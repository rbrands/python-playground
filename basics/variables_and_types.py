#!/usr/bin/env python3
"""
Variables and Data Types in Python
This demonstrates basic Python data types and variable usage.
"""

def main():
    """Demonstrate various Python data types."""
    print("=== Python Variables and Data Types ===\n")
    
    # Integers
    age = 25
    print(f"Integer: age = {age}, type = {type(age)}")
    
    # Floats
    temperature = 23.5
    print(f"Float: temperature = {temperature}, type = {type(temperature)}")
    
    # Strings
    name = "Python"
    greeting = 'Hello, World!'
    print(f"String: name = '{name}', type = {type(name)}")
    
    # Booleans
    is_learning = True
    is_difficult = False
    print(f"Boolean: is_learning = {is_learning}, type = {type(is_learning)}")
    
    # Lists (mutable, ordered)
    fruits = ["apple", "banana", "cherry"]
    print(f"\nList: fruits = {fruits}")
    fruits.append("orange")
    print(f"After append: {fruits}")
    
    # Tuples (immutable, ordered)
    coordinates = (10, 20)
    print(f"\nTuple: coordinates = {coordinates}, type = {type(coordinates)}")
    
    # Dictionaries (key-value pairs)
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(f"\nDictionary: person = {person}")
    print(f"Person's name: {person['name']}")
    
    # Sets (unique, unordered)
    unique_numbers = {1, 2, 3, 3, 4, 5}
    print(f"\nSet: unique_numbers = {unique_numbers}")

if __name__ == "__main__":
    main()
