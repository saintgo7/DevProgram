#!/usr/bin/env python3
"""
RSS Feed Reader
Read RSS feeds
"""

import urllib.request
import urllib.error
from typing import Optional


def fetch_url(url: str) -> Optional[str]:
    """Fetch content from a URL."""
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            return content
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
        return None


def main():
    """Main function."""
    print("=== RSS Feed Reader ===")
    print("Read RSS feeds\n")

    url = input("Enter URL: ").strip()

    if not url:
        print("Error: URL required!")
        return

    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"Fetching: {url}")
    content = fetch_url(url)

    if content:
        print(f"\nReceived {len(content)} characters")
        print(f"\nFirst 500 characters:")
        print(content[:500])
    else:
        print("Failed to fetch URL")


if __name__ == "__main__":
    main()
