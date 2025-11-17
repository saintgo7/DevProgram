#!/usr/bin/env python3
# List Comprehension Examples
def main():
    # Squares
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    
    # Even numbers
    evens = [x for x in range(20) if x % 2 == 0]
    print(f"Evens: {evens}")

if __name__ == "__main__":
    main()
