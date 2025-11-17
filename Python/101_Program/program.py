#!/usr/bin/env python3
# Web Scraper
import urllib.request

def main():
    url = input("Enter URL: ")
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html[:500])  # First 500 chars
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
