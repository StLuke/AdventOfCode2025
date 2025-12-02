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
    return [line.strip() for line in lines if line.strip()]


def process_line(line, current_number):
    """Process a single R/L operation and return new number."""
    if not line:
        return current_number

    direction, number = line[0], int(line[1:])
    return current_number + number if direction == 'R' else current_number - number


def part1(data):
    """Solve part 1 of the puzzle."""
    number = 50
    count = 0

    for line in data:
        number = process_line(line, number)
        if number % 100 == 0:
            count += 1

    return count


def part2(data):
    """Solve part 2 of the puzzle."""
    number = 50
    count = 0
    prev_hundreds = 0  # 50 // 100

    for line in data:
        prev_number = number
        number = process_line(line, number)

        hundreds = number // 100
        if hundreds != prev_hundreds:
            # Calculate boundary crossings with adjustments
            crossings = abs(hundreds - prev_hundreds)

            # Apply L-direction adjustments
            if line[0] == 'L':
                if number % 100 == 0:
                    crossings += 1
                if prev_number % 100 == 0:
                    crossings -= 1

            count += crossings
        elif number % 100 == 0 and line[0] == 'L':
            count += 1

        prev_hundreds = hundreds

    return count


def main():
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 01")
    print("=" * 30)

    try:
        data = read_input("input.txt")
        parsed_data = parse_data(data)

        print(f"Part 1: {part1(parsed_data)}")
        print(f"Part 2: {part2(parsed_data)}")
    except FileNotFoundError:
        print("input.txt not found. Please add your puzzle input.")


if __name__ == "__main__":
    main()
