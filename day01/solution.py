#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 01
https://adventofcode.com/2025/day/1
"""

import os


def read_input(filename="input.txt"):
    """Read and parse the input file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as f:
        return f.read().strip()


def parse_data(data):
    """Parse the input data into a usable format."""
    lines = data.split('\n')
    # TODO: Implement parsing logic based on the actual problem
    return lines


def part1(data):
    """Solve part 1 of the puzzle."""
    # TODO: Implement part 1 solution
    return 0


def part2(data):
    """Solve part 2 of the puzzle."""
    # TODO: Implement part 2 solution
    return 0


def main():
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 01")
    print("=" * 30)

    # Test with example data
    try:
        example_data = read_input("example.txt")
        parsed_example = parse_data(example_data)

        print("Example Results:")
        print(f"Part 1: {part1(parsed_example)}")
        print(f"Part 2: {part2(parsed_example)}")
        print()
    except FileNotFoundError:
        print("No example.txt found, skipping example test")
        print()

    # Solve with actual input
    try:
        actual_data = read_input("input.txt")
        parsed_data = parse_data(actual_data)

        print("Actual Results:")
        print(f"Part 1: {part1(parsed_data)}")
        print(f"Part 2: {part2(parsed_data)}")
    except FileNotFoundError:
        print("input.txt not found. Please add your puzzle input.")


if __name__ == "__main__":
    main()
