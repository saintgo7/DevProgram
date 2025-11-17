#!/usr/bin/env python3
"""
File Comparison
Compare two files
"""

from pathlib import Path


def compare_files(file1: str, file2: str) -> None:
    """Compare two files line by line."""
    try:
        path1 = Path(file1)
        path2 = Path(file2)

        if not path1.exists() or not path2.exists():
            print("Error: One or both files not found!")
            return

        with open(path1, 'r') as f1, open(path2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        if lines1 == lines2:
            print("✓ Files are identical")
            return

        print(f"Files differ:")
        print(f"  {file1}: {len(lines1)} lines")
        print(f"  {file2}: {len(lines2)} lines")

        differences = 0
        for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
            if line1 != line2:
                differences += 1
                if differences <= 10:
                    print(f"\nLine {i} differs:")
                    print(f"  < {line1.rstrip()}")
                    print(f"  > {line2.rstrip()}")

        print(f"\nTotal differences: {differences}")

    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function."""
    print("=== File Comparison ===")
    print("Compare two files\n")

    file1 = input("First file: ").strip()
    file2 = input("Second file: ").strip()

    if file1 and file2:
        compare_files(file1, file2)


if __name__ == "__main__":
    main()
