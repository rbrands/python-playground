#!/usr/bin/env python3
"""
Hello World - The classic first program in Python
This demonstrates the simplest Python program that prints output to the console.
"""

def main():
    """Main function to run the hello world example."""
    print("Hello, World!")
    print("Welcome to the Python Playground!")
    
    # You can also print multiple items
    name = "Python Programmer"
    print("Hello,", name)
    
    # Using f-strings (Python 3.6+)
    version = 3.12
    print(f"You're learning Python {version}!")

if __name__ == "__main__":
    main()
