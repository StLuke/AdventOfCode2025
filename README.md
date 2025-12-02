# Advent of Code 2025

This repository contains solutions for [Advent of Code 2025](https://adventofcode.com/) challenges.

## Project Structure

Each challenge is organized in its own directory:
```
dayXX/
├── solution.py     # Main solution script
├── input.txt       # Puzzle input (not committed to git)
├── example.txt     # Example input from problem description
└── README.md       # Problem description and notes (optional)
```

## Setup

1. **Activate virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running Solutions

Navigate to the specific day's directory and run the solution:
```bash
cd day01
python solution.py
```

## Development Guidelines

- Each solution should be self-contained in its directory
- Follow PEP 8 style guidelines (enforced by flake8)
- Include comments explaining complex algorithms
- Test with both example and actual inputs

## Code Quality

Before committing changes:
```bash
flake8 . --max-line-length=120
```