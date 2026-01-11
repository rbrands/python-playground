#!/usr/bin/env python3
"""
Working with Files in Python
This demonstrates how to read and write files.
"""

import os
import json

def write_text_file():
    """Write a simple text file."""
    filename = "/tmp/sample.txt"
    
    with open(filename, 'w') as file:
        file.write("Hello, World!\n")
        file.write("This is a sample text file.\n")
        file.write("Python makes file handling easy!\n")
    
    print(f"Created {filename}")
    return filename

def read_text_file(filename):
    """Read a text file."""
    print(f"\nReading {filename}:")
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

def read_lines(filename):
    """Read a file line by line."""
    print(f"Reading {filename} line by line:")
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            print(f"  Line {line_num}: {line.strip()}")
    print()

def write_json_file():
    """Write a JSON file."""
    filename = "/tmp/data.json"
    
    data = {
        "name": "Python Playground",
        "version": "1.0",
        "features": ["hello world", "data types", "functions"],
        "stats": {
            "examples": 5,
            "difficulty": "beginner"
        }
    }
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    
    print(f"Created JSON file: {filename}")
    return filename

def read_json_file(filename):
    """Read a JSON file."""
    with open(filename, 'r') as file:
        data = json.load(file)
    
    print(f"\nJSON data from {filename}:")
    print(json.dumps(data, indent=2))
    return data

def main():
    """Demonstrate file operations."""
    print("=== Working with Files ===\n")
    
    # Text files
    txt_file = write_text_file()
    read_text_file(txt_file)
    read_lines(txt_file)
    
    # JSON files
    json_file = write_json_file()
    read_json_file(json_file)
    
    # Cleanup
    print("\nCleaning up temporary files...")
    os.remove(txt_file)
    os.remove(json_file)
    print("Done!")

if __name__ == "__main__":
    main()
