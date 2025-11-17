#!/usr/bin/env python3
# Email Validator
import re

def main():
    email = input("Email: ")
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        print("Valid email!")
    else:
        print("Invalid email!")

if __name__ == "__main__":
    main()
