#!/usr/bin/env python3
"""
Control Flow in Python
This demonstrates if statements, loops, and other control flow constructs.
"""

def demonstrate_if_statements():
    """Show how if/elif/else statements work."""
    print("=== If Statements ===")
    
    age = 18
    if age >= 18:
        print("You are an adult")
    elif age >= 13:
        print("You are a teenager")
    else:
        print("You are a child")
    
    # Ternary operator
    status = "even" if 10 % 2 == 0 else "odd"
    print(f"10 is {status}\n")

def demonstrate_loops():
    """Show different types of loops."""
    print("=== Loops ===")
    
    # For loop with range
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print("\n")
    
    # For loop with list
    fruits = ["apple", "banana", "cherry"]
    print("Fruits:")
    for fruit in fruits:
        print(f"  - {fruit}")
    print()
    
    # For loop with enumerate
    print("Fruits with index:")
    for index, fruit in enumerate(fruits, start=1):
        print(f"  {index}. {fruit}")
    print()
    
    # While loop
    print("Countdown:")
    count = 5
    while count > 0:
        print(count, end=" ")
        count -= 1
    print("Blast off!\n")

def demonstrate_list_comprehension():
    """Show list comprehensions."""
    print("=== List Comprehensions ===")
    
    # Basic list comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")
    
    # List comprehension with condition
    evens = [x for x in range(1, 11) if x % 2 == 0]
    print(f"Even numbers 1-10: {evens}\n")

def main():
    """Run all demonstrations."""
    demonstrate_if_statements()
    demonstrate_loops()
    demonstrate_list_comprehension()

if __name__ == "__main__":
    main()
