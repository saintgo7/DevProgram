#!/usr/bin/env python3
# Password Generator
import random
import string

def main():
    length = int(input("Password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
