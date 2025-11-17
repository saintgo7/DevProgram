#!/usr/bin/env python3
# CSV Writer
import csv

def main():
    data = [
        ['Name', 'Age', 'City'],
        ['John', '30', 'NYC'],
        ['Jane', '25', 'LA']
    ]
    
    with open('output.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    print("CSV file created!")

if __name__ == "__main__":
    main()
