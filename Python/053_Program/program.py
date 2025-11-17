#!/usr/bin/env python3
# CSV Reader
import csv

def main():
    filepath = input("CSV file: ")
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(' | '.join(row))

if __name__ == "__main__":
    main()
