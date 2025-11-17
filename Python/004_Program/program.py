#!/usr/bin/env python3
# File Copy - Copy files
import shutil

def main():
    print("=== File Copy ===")
    source = input("Source file: ")
    dest = input("Destination: ")
    
    try:
        shutil.copy2(source, dest)
        print("File copied successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
