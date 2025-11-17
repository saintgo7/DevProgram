#!/usr/bin/env python3
"""
File Synchronizer
Sync directories
"""

import os
from pathlib import Path


def process_file(filepath: str) -> None:
    """Process a single file."""
    path = Path(filepath)

    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return

    print(f"\nFile: {path.name}")
    print(f"Size: {path.stat().st_size:,} bytes")
    print(f"Type: {path.suffix or 'No extension'}")
    print(f"Path: {path.absolute()}")


def process_directory(directory: str) -> None:
    """Process all files in a directory."""
    path = Path(directory)

    if not path.is_dir():
        print(f"Error: Not a directory: {directory}")
        return

    files = list(path.glob('*'))
    print(f"\nFound {len(files)} items in directory")

    for item in files[:20]:  # Show first 20
        type_str = "DIR" if item.is_dir() else "FILE"
        size = item.stat().st_size if item.is_file() else 0
        print(f"  [{type_str}] {item.name} ({size:,} bytes)")


def main():
    """Main function."""
    print("=== File Synchronizer ===")
    print("Sync directories\n")

    path = input("Enter file or directory path: ").strip()

    if not path:
        print("Error: Path required!")
        return

    path_obj = Path(path)

    if path_obj.is_file():
        process_file(path)
    elif path_obj.is_dir():
        process_directory(path)
    else:
        print(f"Error: Path not found: {path}")


if __name__ == "__main__":
    main()
