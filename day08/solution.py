#!/usr/bin/env python3
"""Advent of Code 2025 - Day 08"""

import os
import math
import heapq
from itertools import product


def euclidean_distance(p1, p2):
    """Calculate 3D Euclidean distance between two points."""
    a1, b1, c1 = p1
    a2, b2, c2 = p2
    return math.sqrt((a1-a2)**2 + (b1-b2)**2 + (c1-c2)**2)


def find_min_distance_and_index(distances, exclude_index):
    """Find minimum distance and its index, excluding self-distance."""
    min_value = float('inf')
    min_index = -1
    for j, distance in enumerate(distances):
        if j != exclude_index and distance < min_value:
            min_value = distance
            min_index = j
    return min_value, min_index


def load_data(filename="input.txt"):
    """Load and parse input data into circuit graph structure.

    Returns:
        circuit_graph: List of circuits, where each circuit is:
        [
            node_coordinates_list,  # [(x,y,z), (x,y,z), ...] - all coordinate points in this circuit
            distance_array,         # [dist_to_0, dist_to_1, ...] - distances to other circuits
            min_distance_info       # (min_dist, target_index, current_x, target_x) - added later
        ]
    """
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(filepath):
        filepath = os.path.join(os.path.dirname(__file__), "example.txt")

    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')

    # Parse each line into a tuple of 3 integers
    data = []
    for line in lines:
        numbers = tuple(int(x) for x in line.split(','))
        data.append(numbers)

    # Add a list of X -1s to each tuple, where X is the number of tuples
    X = len(data)
    paths = [-1] * X

    # Convert each tuple to structure [node, paths]
    # node: [(a, b, c)] - coordinates list
    # paths: [dist_to_0, dist_to_1, ...] - distances to other nodes
    circuit_graph = []
    for i, numbers in enumerate(data):
        current_paths = paths.copy()
        current_paths[i] = 0  # Set N-th element to 0, where N is current index
        node = [numbers]  # First element: node coordinates
        paths_list = current_paths  # Second element: paths distances
        circuit_structure = [node, paths_list]
        circuit_graph.append(circuit_structure)

    # Calculate distances from tuple 0 to all other tuples
    if len(circuit_graph) > 0:
        first_tuple_coords = circuit_graph[0][0][0]  # (a1, b1, c1)
        a1, b1, c1 = first_tuple_coords

        for i in range(1, len(circuit_graph)):
            other_tuple_coords = circuit_graph[i][0][0]  # (a2, b2, c2)
            a2, b2, c2 = other_tuple_coords

            # Calculate 3D Euclidean distance
            distance = euclidean_distance(first_tuple_coords, other_tuple_coords)

            # Store distance at i-th position in first tuple's paths
            circuit_graph[0][1][i] = distance

            # Store distance at 0-th position in i-th tuple's paths
            circuit_graph[i][1][0] = distance

    return circuit_graph


def solve_part1(circuit_data):
    """Solve part 1 of the puzzle."""
    if len(circuit_data) == 0:
        return 0

    # Calculate distances between all pairs of nodes
    for i, circuit_i in enumerate(circuit_data):
        node_i = circuit_i[0][0]  # Access: circuit[0][0] = first coordinate in first circuit's coordinate list
        a1, b1, c1 = node_i

        for j, circuit_j in enumerate(circuit_data):
            if i != j:  # Don't calculate distance to itself
                node_j = circuit_j[0][0]  # Access: circuit[0][0] = first coordinate in second circuit's coordinate list
                a2, b2, c2 = node_j

                # Calculate 3D Euclidean distance
                distance = euclidean_distance(node_i, node_j)

                # Store distance in distance array
                paths = circuit_i[1]  # Access: circuit[1] = distance array to other circuits
                paths[j] = distance

    # Find 1000 lowest distances between all node pairs using generator + heapq
    all_distances = ((circuit_data[i][1][j], i, j)
                     for i in range(len(circuit_data))
                     for j in range(i + 1, len(circuit_data[i][1])))
    lowest_1000_distances = heapq.nsmallest(1000, all_distances)

    # Group nodes based on shortest distances
    node_lists = []  # List of lists, each containing connected node indices

    for idx, (dist, node1, node2) in enumerate(lowest_1000_distances):
        # Find which lists contain node1 and node2
        list1_idx = None
        list2_idx = None

        for i, node_list in enumerate(node_lists):
            if node1 in node_list:
                list1_idx = i
            if node2 in node_list:
                list2_idx = i

        # Both nodes in same list - do nothing
        if list1_idx is not None and list1_idx == list2_idx:
            continue

        # Both nodes in different lists - merge lists
        elif list1_idx is not None and list2_idx is not None:
            node_lists[list1_idx].extend(node_lists[list2_idx])
            node_lists.pop(list2_idx)

        # One node in list, add the other
        elif list1_idx is not None:
            node_lists[list1_idx].append(node2)

        elif list2_idx is not None:
            node_lists[list2_idx].append(node1)

        # Neither node in any list - create new list
        else:
            node_lists.append([node1, node2])

    # Sort groups by size (largest to smallest)
    node_lists.sort(key=len, reverse=True)

    # Calculate product of group sizes using math.prod
    if len(node_lists) >= 3:
        result = math.prod(len(node_lists[i]) for i in range(3))
    else:
        # Handle case where there are fewer than 3 groups
        result = math.prod(len(node_list) for node_list in node_lists)

    # Add minimal path information to each circuit (extends structure to have 3rd element)
    for i, circuit in enumerate(circuit_data):
        paths = circuit[1]  # Access: circuit[1] = distance array to other circuits

        # Find the minimum distance (excluding distance to itself at index i)
        min_dist_value, min_dist_index = find_min_distance_and_index(paths, i)

        # Add min_distance info as 3rd element: (min_dist, target_index, current_x, target_x)
        current_x = circuit[0][0][0]  # Access: circuit[0][0][0] = X coordinate of first node in circuit
        target_x = circuit_data[min_dist_index][0][0][0] if min_dist_index != -1 else -1  # X coordinate of target circuit's first node
        min_distance = (min_dist_value, min_dist_index, current_x, target_x)
        circuit.append(min_distance)  # Now circuit structure is: [coords_list, distances, min_distance_info]

    return result


def solve_part2(circuit_data):
    """Solve part 2 of the puzzle - hierarchical clustering with merging."""
    print(f"Part 2: Starting hierarchical clustering with {len(circuit_data)} points")

    # Continue merging until only 2 groups remain
    iteration = 0
    while len(circuit_data) > 2:
        iteration += 1
        current_global_min_distance = float('inf')
        current_global_min_from_index = -1
        current_global_min_to_index = -1

        for i, circuit in enumerate(circuit_data):
            min_distance = circuit[2]  # Access: circuit[2] = min_distance_info tuple (dist, target_index, curr_x, target_x)
            min_dist_value, min_dist_index = min_distance[0], min_distance[1]

            if min_dist_value < current_global_min_distance:
                current_global_min_distance = min_dist_value
                current_global_min_from_index = i
                current_global_min_to_index = min_dist_index

        if current_global_min_from_index == -1 or len(circuit_data) <= 1:
            break

        # Determine lower and higher index
        lower_index = min(current_global_min_from_index, current_global_min_to_index)
        higher_index = max(current_global_min_from_index, current_global_min_to_index)

        # Step 1: Add ALL coordinates from higher index node to lower index node
        higher_node_coords_list = circuit_data[higher_index][0]  # Get all coordinates from higher node
        circuit_data[lower_index][0].extend(higher_node_coords_list)  # Add all of them to lower node

        # Step 2: Remove higher index position from all paths lists
        for i, circuit in enumerate(circuit_data):
            circuit[1].pop(higher_index)

        # Step 3: Merge paths of the two chosen nodes (take minimum distances)
        lower_paths = circuit_data[lower_index][1]
        higher_paths = circuit_data[higher_index][1]

        for j in range(len(lower_paths)):
            if j < len(higher_paths):  # Safety check
                if j == lower_index:
                    # Distance to itself remains 0
                    lower_paths[j] = 0
                else:
                    # Take minimum of the two distances
                    lower_paths[j] = min(lower_paths[j], higher_paths[j])

        # Step 4: Update all other nodes' paths to reflect the merger
        for i, circuit in enumerate(circuit_data):
            if i != lower_index and i < len(circuit_data):
                # Update distance to merged node (take minimum)
                if lower_index < len(circuit[1]):
                    current_dist_to_lower = circuit[1][lower_index]

                    # Find minimum distance from ANY coordinate in node i to ANY coordinate in higher node
                    other_node_coords_list = circuit[0]
                    min_dist_to_higher = min(euclidean_distance(other_coord, higher_coord)
                                           for other_coord, higher_coord in product(other_node_coords_list, higher_node_coords_list))

                    # Take minimum distance (single-linkage clustering)
                    circuit[1][lower_index] = min(current_dist_to_lower, min_dist_to_higher)

        # Step 5: Remove the higher index node completely
        circuit_data.pop(higher_index)

        # Step 6: Recalculate min_distance for all remaining nodes
        for i, circuit in enumerate(circuit_data):
            paths = circuit[1]
            min_dist_value, min_dist_index = find_min_distance_and_index(paths, i)

            # Find actual nodes with minimum distance and their X coordinates
            if min_dist_index != -1:
                # Find the actual pair of nodes that have this minimum distance
                current_nodes = circuit[0]
                target_nodes = circuit_data[min_dist_index][0]

                best_current_x = current_nodes[0][0]  # Default to first node
                best_target_x = target_nodes[0][0]    # Default to first node
                actual_min_dist = float('inf')

                # Find the actual pair with minimum distance
                min_pair = min(((euclidean_distance(curr_coord, target_coord), curr_coord, target_coord)
                              for curr_coord, target_coord in product(current_nodes, target_nodes)))
                actual_min_dist, best_curr_coord, best_target_coord = min_pair
                best_current_x = best_curr_coord[0]  # X coordinate of current coord
                best_target_x = best_target_coord[0]  # X coordinate of target coord

                circuit[2] = (min_dist_value, min_dist_index, best_current_x, best_target_x)
            else:
                circuit[2] = (min_dist_value, min_dist_index, -1, -1)

        print(f"Iteration {iteration}: {len(circuit_data)} groups remaining")

    # Calculate result by multiplying X coordinates of smallest distance nodes from final 2 groups
    if len(circuit_data) == 2:
        x1 = circuit_data[0][2][2]  # X coordinate of group 0's smallest distance node
        x2 = circuit_data[1][2][2]  # X coordinate of group 1's smallest distance node
        result = x1 * x2
        return result
    else:
        return len(circuit_data)


if __name__ == "__main__":
    circuit_graph = load_data("input.txt")

    part1_result = solve_part1(circuit_graph)
    part2_result = solve_part2(circuit_graph)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")
