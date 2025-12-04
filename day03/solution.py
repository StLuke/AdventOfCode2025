#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 03
"""

import os
from typing import List


def read_input(filename: str = "input.txt") -> str:
    """Read input file."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, 'r') as f:
        return f.read().strip()


def parse_data(data: str) -> List[str]:
    """Parse newline-separated strings of digits."""
    lines = data.strip().split('\n')
    return [line.strip() for line in lines if line.strip()]


def part1(data: List[str]) -> int:
    """Solve part 1 of the puzzle."""
    total_sum = 0

    for number_str in data:
        search_range = number_str[:-1]
        first_digit = max(search_range)
        first_pos = number_str.index(first_digit)
        value = int(first_digit + max(number_str[first_pos+1:]))

        total_sum += value

    return total_sum


def part2(data: List[str]) -> int:
    """Solve part 2 of the puzzle."""
    total_sum = 0

    for number_str in data:
        digits = []
        start_pos = 0

        for i in range(12):
            end_offset = 11 - i
            search_range = number_str[start_pos:-end_offset] if end_offset > 0 else number_str[start_pos:]

            if search_range:
                max_digit = max(search_range)
                digits.append(max_digit)
                found_pos = number_str.index(max_digit, start_pos)
                start_pos = found_pos + 1
            else:
                break

        if digits:
            value = int(''.join(digits))
            total_sum += value

    return total_sum


def main() -> None:
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 03")
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
