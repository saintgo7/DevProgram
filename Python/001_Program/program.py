#!/usr/bin/env python3
# File Reader - Read and display file contents
import os

def main():
    print("=== File Reader ===")
    filepath = input("Enter file path: ")
    
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')
            
        print(f"\n--- File Contents ---")
        print(content)
        print(f"\n--- Statistics ---")
        print(f"Total lines: {len(lines)}")
        print(f"Total characters: {len(content)}")
        print(f"File size: {os.path.getsize(filepath)} bytes")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
