#!/usr/bin/env python3
"""
Data Processor 98
Data processing tool 98
"""

import json
from typing import Dict, List, Any


def process_data(data: List[Dict[str, Any]]) -> None:
    """Process and analyze data."""
    print(f"\nProcessing {len(data)} records...")

    # Basic statistics
    if data:
        print(f"Fields: {', '.join(data[0].keys())}")

        # Count records
        print(f"Total records: {len(data)}")

        # Show sample
        print("\nSample records:")
        for i, record in enumerate(data[:3], 1):
            print(f"  {i}. {record}")


def main():
    """Main function."""
    print("=== Data Processor 98 ===")
    print("Data processing tool 98\n")

    # Sample data
    sample_data = [
        {"id": 1, "name": "Item 1", "value": 100},
        {"id": 2, "name": "Item 2", "value": 200},
        {"id": 3, "name": "Item 3", "value": 150},
    ]

    print("Sample data loaded")
    process_data(sample_data)

    # Export option
    export = input("\nExport to JSON? (y/n): ").strip().lower()
    if export == 'y':
        filename = input("Filename: ").strip()
        if filename:
            with open(filename, 'w') as f:
                json.dump(sample_data, f, indent=2)
            print(f"Exported to {filename}")


if __name__ == "__main__":
    main()
