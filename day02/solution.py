#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 02
"""

import os
import pprint
import re


def read_input(filename="input.txt"):
    """Read input file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as f:
        return f.read().strip()


def parse_data(data):
    """Parse comma-separated ranges into tuples."""
    ranges = []
    for range_str in data.split(','):
        start, end = range_str.split('-')
        ranges.append((int(start), int(end)))
    return ranges


def part1(data):
    """Solve part 1 of the puzzle."""
    total_sum = 0

    for start, end in data:
        start_digits = len(str(start))
        end_digits = len(str(end))

        # Adjust ranges based on digit count characteristics
        if start_digits % 2 != 0:
            start = 10 ** start_digits
        if end_digits % 2 != 0:
            end = 10 ** (end_digits - 1) - 1

        if start <= end:
            start_str = str(start)
            end_str = str(end)

            start_half_digits = len(start_str) // 2
            end_half_digits = len(end_str) // 2

            start_first_half = int(start_str[:start_half_digits]) if start_half_digits > 0 else 0
            end_first_half = int(end_str[:end_half_digits]) if end_half_digits > 0 else 0

            # Generate invalid IDs by doubling digits
            invalid_ids = []
            for num in range(start_first_half, end_first_half + 1):
                num_str = str(num)
                doubled_str = num_str + num_str
                invalid_id = int(doubled_str)

                if start <= invalid_id <= end:
                    invalid_ids.append(invalid_id)

            invalid_ids_sum = sum(invalid_ids)
            total_sum += invalid_ids_sum

    return total_sum


def part2(data):
    """Solve part 2 of the puzzle."""
    # Regex pattern matches numbers with repeating patterns (e.g., 123123, 77, 999999)
    pattern = r"^(.+)\1+$"
    regex = re.compile(pattern)

    total_sum = 0

    for start, end in data:
        matching_numbers = []

        for num in range(start, end + 1):
            num_str = str(num)
            if regex.match(num_str):
                matching_numbers.append(num)

        matching_sum = sum(matching_numbers)
        total_sum += matching_sum

    # oh bite me, I like part 1 solution better
    return total_sum


def main():
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 02")
    print("=" * 30)

    try:
        data = read_input("input.txt")
        parsed_data = parse_data(data)

        print("Part 1:")
        pprint.pprint(part1(parsed_data))
        print(f"\nPart 2: {part2(parsed_data)}")
    except FileNotFoundError:
        print("input.txt not found. Please add your puzzle input.")


if __name__ == "__main__":
    main()
