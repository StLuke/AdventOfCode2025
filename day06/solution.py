#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 06
"""

import os
import re
import math


def load_input_data(parse_as_numbers=True):
    """Unified input loader with flexible parsing."""
    filename = "input.txt" if os.path.exists(os.path.join(os.path.dirname(__file__), "input.txt")) else "example.txt"
    with open(os.path.join(os.path.dirname(__file__), filename), 'r') as f:
        lines = f.read().strip().split('\n')

    raw_lines = [line for line in lines[:-1] if line.strip()]
    symbol_line = lines[-1]

    if parse_as_numbers:
        # Part 1: Convert lines to integer matrix, symbols to list
        matrix = [[int(x) for x in line.split()] for line in raw_lines]
        symbols = symbol_line.split()
        return matrix, symbols
    else:
        # Part 2: Extract symbols and calculate spacing between them
        symbols = re.findall(r'\S', symbol_line)
        spacing = [len(m.group()) for m in re.finditer(r' +', symbol_line)]
        return raw_lines, symbols, spacing


def apply_operations(data, symbols, axis='column'):
    """Apply symbol operations to data along specified axis."""
    operations = {'+': sum, '*': math.prod}

    results = []
    for i, symbol in enumerate(symbols):
        # Extract values based on axis: columns vs rows
        if axis == 'column':
            values = [row[i] for row in data if i < len(row)]  # Get column i from all rows
        else:
            values = data[i] if i < len(data) else []  # Get row i

        # Apply operation (+sum or *product) to the values
        results.append(operations[symbol](values))
    return results


def parse_segments(line, spacing):
    """Parse line into segments based on spacing."""
    segments = []
    pos = 0  # Current position in line

    # Extract each segment based on spacing
    for space_count in spacing:
        segment = line[pos:pos + space_count] if pos < len(line) else ""
        segments.append(segment)
        pos += space_count + 1  # Move past segment + 1 space

    # Add final segment (everything after last space)
    final_segment = line[pos:] if pos < len(line) else ""
    segments.append(final_segment)
    return segments

def transpose_and_segment(raw_lines, spacing):
    """Parse lines into segments and perform double transpose."""
    if not raw_lines:
        return []

    # Step 1: Parse each line into segments based on spacing
    segments = [parse_segments(line, spacing) for line in raw_lines]

    result = []
    # Step 2: First transpose - group segments by column position
    for col in range(len(segments[0])):
        col_segments = [row[col] if col < len(row) else '' for row in segments]
        max_len = max(len(s) for s in col_segments) if col_segments else 0

        # Step 3: Second transpose - group characters by position within segments
        int_row = []
        for pos in range(max_len):
            # Collect characters at position 'pos' from all segments in this column
            char_str = ''.join(s[pos] if pos < len(s) else ' ' for s in col_segments).strip()
            if char_str:  # Convert to integer if non-empty
                int_row.append(int(char_str))
        result.append(int_row)

    return result


def part1():
    """Part 1: Column operations on number matrix."""
    matrix, symbols = load_input_data(parse_as_numbers=True)
    return sum(apply_operations(matrix, symbols, axis='column'))


def part2():
    """Part 2: Row operations on transposed character matrix."""
    raw_lines, symbols, spacing = load_input_data(parse_as_numbers=False)
    return sum(apply_operations(transpose_and_segment(raw_lines, spacing), symbols, axis='row'))


def main():
    """Main function to run the solution."""
    print("Advent of Code 2025 - Day 06")
    print("=" * 30)

    print("Part 1:")
    print(f"Result: {part1()}")

    print(f"\nPart 2:")
    print(f"Result: {part2()}")


if __name__ == "__main__":
    main()
