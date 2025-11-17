#!/usr/bin/env python3
"""
Context Manager
Custom context managers
"""

import time
from functools import wraps
from typing import Callable, Any


def timer_decorator(func: Callable) -> Callable:
    """Decorator to measure function execution time."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f}s")
        return result
    return wrapper


@timer_decorator
def example_function(n: int) -> int:
    """Example function with decorator."""
    time.sleep(0.1)
    return sum(range(n))


def main():
    """Main function."""
    print("=== Context Manager ===")
    print("Custom context managers\n")

    # Demonstrate decorator
    result = example_function(1000)
    print(f"Result: {result}")

    # Demonstrate list comprehension
    squares = [x**2 for x in range(10)]
    print(f"\nSquares: {squares}")

    # Demonstrate lambda
    double = lambda x: x * 2
    print(f"Double of 5: {double(5)}")


if __name__ == "__main__":
    main()
