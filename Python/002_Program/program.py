#!/usr/bin/env python3
# File Writer - Write text to file
def main():
    print("=== File Writer ===")
    filepath = input("Enter file path: ")
    print("Enter text (type 'END' to finish):")
    
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(lines))
    
    print("File saved successfully!")

if __name__ == "__main__":
    main()
