#!/usr/bin/env python3

import os


def lines_intersect(rect_edge, poly_edge):
    (rx1, ry1), (rx2, ry2) = rect_edge
    (px1, py1), (px2, py2) = poly_edge

    if rect_edge == poly_edge or rect_edge == (poly_edge[1], poly_edge[0]):
        return -1

    rect_horizontal = (ry1 == ry2)
    poly_horizontal = (py1 == py2)

    if rect_horizontal == poly_horizontal:
        return 0
    if rect_horizontal:
        h_left, h_right = sorted([rx1, rx2])
        h_y = ry1
        v_bottom, v_top = sorted([py1, py2])
        v_x = px1
    else:
        h_left, h_right = sorted([px1, px2])
        h_y = py1
        v_bottom, v_top = sorted([ry1, ry2])
        v_x = rx1

    if h_left < v_x < h_right and v_bottom < h_y < v_top:
        return 1
    if rect_horizontal:
        if (h_y == v_bottom or h_y == v_top) and h_left <= v_x <= h_right:
            return -1
    else:
        if (v_x == h_left or v_x == h_right) and v_bottom <= h_y <= v_top:
            return -1

    return 0


def point_inside_rectangle(point, rect_corners):
    x, y = point
    bottom_left, bottom_right, top_right, top_left = rect_corners
    min_x, max_x = bottom_left[0], top_right[0]
    min_y, max_y = bottom_left[1], top_right[1]
    return min_x < x < max_x and min_y < y < max_y



def check_rectangle_intersections(rectangle_corners, polygon_data):
    bl, br, tr, tl = rectangle_corners
    rectangle_edges = [(bl, br), (br, tr), (tr, tl), (tl, bl)]
    polygon_edges = [(polygon_data[i], polygon_data[(i + 1) % len(polygon_data)]) for i in range(len(polygon_data))]

    for poly_edge in polygon_edges:
        for rect_edge in rectangle_edges:
            if lines_intersect(rect_edge, poly_edge) == 1:
                return True

        poly_point1, poly_point2 = poly_edge
        if (point_inside_rectangle(poly_point1, rectangle_corners) or
            point_inside_rectangle(poly_point2, rectangle_corners)):
            return True

        touching_count = 0
        for rect_edge in rectangle_edges:
            if lines_intersect(rect_edge, poly_edge) == -1:
                touching_count += 1

        if touching_count > 1:
            is_coincident = any(poly_edge == rect_edge or poly_edge == (rect_edge[1], rect_edge[0])
                              for rect_edge in rectangle_edges)
            if not is_coincident:
                return True

    return False


def rectangle_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def rectangle_corners(p1, p2):
    xs, ys = sorted([p1[0], p2[0]]), sorted([p1[1], p2[1]])
    return [(xs[0], ys[0]), (xs[1], ys[0]), (xs[1], ys[1]), (xs[0], ys[1])]


def generate_rectangles(nodes):
    return [
        (rectangle_area(nodes[i], nodes[j]), rectangle_corners(nodes[i], nodes[j]))
        for i in range(len(nodes))
        for j in range(i + 1, len(nodes))
    ]


def load_data(filename="input.txt"):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(filepath):
        filepath = os.path.join(os.path.dirname(__file__), "example.txt")

    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')

    coordinates = []
    for line in lines:
        if line.strip():
            x, y = map(int, line.split(','))
            coordinates.append((x, y))

    return coordinates


def solve_part1(data):
    if not data:
        return 0

    sorted_nodes = sorted(data)
    max_area = 0

    for i in range(len(sorted_nodes)):
        for j in range(i + 1, len(sorted_nodes)):
            area = rectangle_area(sorted_nodes[i], sorted_nodes[j])
            if area > max_area:
                max_area = area

    return max_area


def solve_part2(data):
    if not data:
        return 0

    rectangles = generate_rectangles(sorted(data))
    rectangles.sort(key=lambda x: x[0], reverse=True)

    return next((area for area, corners in rectangles
                 if not check_rectangle_intersections(corners, data)), 0)


if __name__ == "__main__":
    data = load_data()

    part1_result = solve_part1(data)
    part2_result = solve_part2(data)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")