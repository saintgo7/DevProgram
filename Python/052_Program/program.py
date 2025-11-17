#!/usr/bin/env python3
# JSON Writer
import json

def main():
    data = {"name": "John", "age": 30, "city": "NYC"}
    json_str = json.dumps(data, indent=2)
    print(json_str)

if __name__ == "__main__":
    main()
