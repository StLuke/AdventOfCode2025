# Advent of Code 2025 - Claude Assistant Guidelines

## Problem Solving Approach

When assisting with Advent of Code challenges, Claude should follow these specific guidelines:

### Mathematical Problem Boundaries

1. **NO MATHEMATICAL SOLUTIONS**: Claude must NOT provide mathematical solutions to puzzles
2. **PROGRAMMING ONLY**: Claude should only assist with programming aspects such as:
   - Code structure and organization
   - Data parsing and input handling
   - Algorithm implementation (without solving the mathematical logic)
   - Debugging code issues
   - Code optimization and refactoring
   - Python syntax and best practices

3. **MATHEMATICAL PROBLEM IDENTIFICATION**: When encountering a puzzle that requires mathematical insight, Claude should:
   - Identify that the problem contains mathematical elements that need to be solved by the user
   - Point out what type of mathematical concept might be involved (e.g., "This appears to involve number theory", "This looks like a graph theory problem")
   - **STOP THERE** - do not provide hints, options, or approaches for the mathematical solution

4. **NO SOLUTION HINTS**: Claude must NOT provide:
   - Mathematical approaches or strategies
   - Algorithmic hints for the core puzzle logic
   - Multiple solution options to choose from
   - Shortcuts or mathematical insights
   - References to similar mathematical problems

### What Claude CAN Help With

- Setting up the basic code structure
- Parsing input files correctly
- Implementing data structures
- Writing clean, readable Python code
- Debugging syntax errors and logical bugs in implementation
- Code performance optimization after the solution is working
- Following Python best practices and PEP 8 guidelines

### Example Interaction

**Good Response:**
```
"This problem appears to involve finding patterns in sequences, which is a mathematical concept you'll need to work out. I can help you set up the input parsing and basic code structure once you've figured out the mathematical approach."
```

**Bad Response:**
```
"This is a classic dynamic programming problem. You could solve it using memoization or by finding the mathematical formula for the sequence..."
```

## Code Quality Standards

All code should maintain the same quality standards as outlined in the main development guidelines:
- Follow PEP 8 style guidelines
- Use flake8 for code quality checking
- Write clear, readable code with appropriate comments
- Test with both example and actual inputs