#!/usr/bin/env python3
# File Search - Search files by pattern
import os
import fnmatch

def main():
    print("=== File Search ===")
    directory = input("Directory: ")
    pattern = input("Pattern (e.g., *.txt): ")
    
    matches = []
    for root, dirs, files in os.walk(directory):
        for filename in fnmatch.filter(files, pattern):
            matches.append(os.path.join(root, filename))
    
    print(f"\nFound {len(matches)} files:")
    for match in matches:
        print(match)

if __name__ == "__main__":
    main()
