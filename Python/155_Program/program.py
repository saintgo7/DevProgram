#!/usr/bin/env python3
# Context Manager Example
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

def main():
    with FileManager('test.txt') as f:
        f.write('Hello, World!')
    print("File written with context manager!")

if __name__ == "__main__":
    main()
