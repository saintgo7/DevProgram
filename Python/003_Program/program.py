#!/usr/bin/env python3
# Directory Lister - List files and directories
import os

def main():
    print("=== Directory Lister ===")
    path = input("Enter directory path: ")
    
    if os.path.isdir(path):
        print(f"\nContents of {path}:")
        print("\nFiles:")
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                print(f"  {item} - {size} bytes")
        
        print("\nDirectories:")
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            if os.path.isdir(full_path):
                print(f"  {item}/")
    else:
        print("Directory not found!")

if __name__ == "__main__":
    main()
