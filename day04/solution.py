#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 04
"""

import os
from typing import List


def read_input(filename: str = "input.txt") -> str:
    """Read input file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as f:
        return f.read().strip()


def parse_data(data: str) -> List[List[int]]:
    """Parse input data into integer matrix where '@' = 1, '.' = 0."""
    lines = data.strip().split('\n')
    matrix = []
    for line in lines:
        if line.strip():
            row = [1 if char == '@' else 0 for char in line.strip()]
            matrix.append(row)
    return matrix


def get_neighbor_sum(matrix: List[List[int]], row: int, col: int) -> int:
    """Calculate sum of 8 neighboring cells."""
    rows, cols = len(matrix), len(matrix[0])
    neighbor_sum = 0

    for row_offset in [-1, 0, 1]:
        for col_offset in [-1, 0, 1]:
            if row_offset == 0 and col_offset == 0:
                continue

            new_row, new_col = row + row_offset, col + col_offset
            if 0 <= new_row < rows and 0 <= new_col < cols:
                neighbor_sum += matrix[new_row][new_col]

    return neighbor_sum


def solve_matrix(data: List[List[int]], iterative: bool = False) -> int:
    """Solve matrix problem with optional iterative mode."""
    rows, cols = len(data), len(data[0])
    matrix = [row[:] for row in data]
    counter = 0

    changed = True
    while changed:
        changed = False
        positions_to_change = []

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 1:
                    continue

                if get_neighbor_sum(matrix, row, col) < 4:
                    counter += 1
                    if iterative:
                        positions_to_change.append((row, col))

        if iterative and positions_to_change:
            changed = True
            for r, c in positions_to_change:
                matrix[r][c] = 0
        else:
            break

    return counter


def part1(data: List[List[int]]) -> int:
    """Count cells where sum of 8 neighbors is less than 4."""
    return solve_matrix(data, iterative=False)


def part2(data: List[List[int]]) -> int:
    """Iteratively count and remove cells where sum of 8 neighbors is less than 4."""
    return solve_matrix(data, iterative=True)


def main() -> None:
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 04")
    print("=" * 30)

    try:
        data = read_input("input.txt")
        parsed_data = parse_data(data)

        print("Part 1:")
        result1 = part1(parsed_data)
        print(result1)

        print(f"\nPart 2:")
        result2 = part2(parsed_data)
        print(result2)
    except FileNotFoundError:
        print("input.txt not found. Please add your puzzle input.")


if __name__ == "__main__":
    main()
