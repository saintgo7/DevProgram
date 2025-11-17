#!/usr/bin/env python3
# JSON Reader
import json

def main():
    data = '{"name": "John", "age": 30, "city": "NYC"}'
    obj = json.loads(data)
    print(f"Name: {obj['name']}")
    print(f"Age: {obj['age']}")
    print(f"City: {obj['city']}")

if __name__ == "__main__":
    main()
