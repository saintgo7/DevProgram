#!/usr/bin/env python3
# XML Parser
import xml.etree.ElementTree as ET

def main():
    xml_data = '<person><name>John</name><age>30</age></person>'
    root = ET.fromstring(xml_data)
    print(f"Name: {root.find('name').text}")
    print(f"Age: {root.find('age').text}")

if __name__ == "__main__":
    main()
