#!/usr/bin/env python3
# URL Download
import urllib.request

def main():
    url = input("URL: ")
    filename = input("Save as: ")
    urllib.request.urlretrieve(url, filename)
    print(f"Downloaded to {filename}")

if __name__ == "__main__":
    main()
