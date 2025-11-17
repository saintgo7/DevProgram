#!/usr/bin/env python3
"""
Generator Example
Python generators
"""

from typing import Generator, Iterator


def fibonacci(n: int) -> Generator[int, None, None]:
    """Generate Fibonacci sequence using generator."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def read_large_file(filename: str) -> Generator[str, None, None]:
    """Read large file line by line efficiently."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File not found: {filename}")


def main():
    """Main function."""
    print("=== Generator Example ===")
    print("Python generators\n")

    # Fibonacci generator example
    print("Fibonacci sequence (first 10):")
    for i, num in enumerate(fibonacci(10), 1):
        print(f"  {i}. {num}")

    # Generator expression example
    print("\nSquares of even numbers (0-20):")
    squares = (x**2 for x in range(21) if x % 2 == 0)
    print(f"  {list(squares)}")


if __name__ == "__main__":
    main()
