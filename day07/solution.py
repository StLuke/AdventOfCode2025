#!/usr/bin/env python3
"""Advent of Code 2025 - Day 07"""

import os


def load_data(filename="input.txt"):
    """Load and parse input into list of S/^ indexes per line."""
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if not os.path.exists(filepath):
        filepath = os.path.join(os.path.dirname(__file__), "example.txt")
    with open(filepath, 'r') as f:
        return [[i for i, c in enumerate(line) if c in 'S^']
                for line in f.read().strip().split('\n')]


def solve(data):
    """Solve both parts in single traversal."""
    tachyon = {idx: 1 for idx in data[0]}
    splits = 0

    for row_indexes in data[1:]:
        row_set = set(row_indexes)
        new_tachyon = {}
        for idx, count in tachyon.items():
            if idx in row_set:
                splits += 1
                new_tachyon[idx - 1] = new_tachyon.get(idx - 1, 0) + count
                new_tachyon[idx + 1] = new_tachyon.get(idx + 1, 0) + count
            else:
                new_tachyon[idx] = new_tachyon.get(idx, 0) + count
        tachyon = new_tachyon

    return splits, sum(tachyon.values())


if __name__ == "__main__":
    print("Advent of Code 2025 - Day 07\n" + "=" * 30)
    part1, part2 = solve(load_data())
    print(f"Part 1: {part1}\nPart 2: {part2}")
