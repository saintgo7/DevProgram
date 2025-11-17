#!/usr/bin/env python3
"""
File Move Tool
Move files between directories
"""

import os
import shutil
from pathlib import Path


def move_file(source: str, destination: str) -> None:
    """Move a file from source to destination."""
    try:
        source_path = Path(source)
        dest_path = Path(destination)

        if not source_path.exists():
            print(f"Error: Source file '{source}' not found!")
            return

        if dest_path.is_dir():
            dest_path = dest_path / source_path.name

        shutil.move(str(source_path), str(dest_path))
        print(f"Moved: {source} -> {dest_path}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function."""
    print("=== File Move Tool ===")
    print("Move files between directories\n")

    source = input("Source file path: ").strip()
    destination = input("Destination path: ").strip()

    if source and destination:
        move_file(source, destination)
    else:
        print("Error: Both source and destination required!")


if __name__ == "__main__":
    main()
