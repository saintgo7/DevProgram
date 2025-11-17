#!/usr/bin/env python3
# Lambda Functions
def main():
    square = lambda x: x**2
    print(f"Square of 5: {square(5)}")
    
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(f"Squared: {squared}")

if __name__ == "__main__":
    main()
