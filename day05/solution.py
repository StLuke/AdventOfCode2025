#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 05
"""

import os


def read_input(filename="input.txt"):
    """Read input file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as f:
        return f.read().strip()


def parse_data(data):
    """Parse ranges and numbers from input."""
    lines = data.split('\n')
    ranges = []

    # Process range lines until empty line
    i = 0
    while i < len(lines) and lines[i].strip():
        line = lines[i].strip()
        new_range = (int(line.split('-')[0]), int(line.split('-')[1]))

        # Merge with overlapping ranges (handles fully contained ranges automatically)
        min_val, max_val = new_range
        to_remove = []

        for j, existing_range in enumerate(ranges):
            # Check if ranges overlap: not (r1[1] < r2[0] or r2[1] < r1[0])
            if not (new_range[1] < existing_range[0] or existing_range[1] < new_range[0]):
                min_val = min(min_val, existing_range[0])
                max_val = max(max_val, existing_range[1])
                to_remove.append(j)

        # Remove merged ranges
        for j in reversed(to_remove):
            ranges.pop(j)

        ranges.append((min_val, max_val))

        i += 1

    # Parse numbers after empty line
    i += 1  # Skip empty line
    numbers = [int(line.strip()) for line in lines[i:] if line.strip()]

    return ranges, numbers


def part1(ranges, numbers):
    """Count numbers within ranges."""
    counter = 0
    for number in numbers:
        for range_tuple in ranges:
            if range_tuple[0] <= number <= range_tuple[1]:
                counter += 1
                break
    return counter


def part2(ranges):
    """Sum of range spans plus count of ranges."""
    return sum(max_val - min_val for min_val, max_val in ranges) + len(ranges)


def main():
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 05")
    print("=" * 30)

    try:
        data = read_input("input.txt")
        ranges, numbers = parse_data(data)

        print("Part 1:")
        result1 = part1(ranges, numbers)
        print(result1)

        print(f"\nPart 2:")
        result2 = part2(ranges)
        print(result2)

    except FileNotFoundError:
        print("input.txt not found. Please add your puzzle input.")


if __name__ == "__main__":
    main()
