#!/usr/bin/env python3
"""
Functions in Python
This demonstrates how to define and use functions in Python.
"""

def greet(name):
    """A simple function that greets someone."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers together."""
    return a + b

def multiply(a, b=1):
    """Multiply two numbers with a default parameter."""
    return a * b

def calculate_stats(*numbers):
    """Calculate statistics for any number of arguments."""
    if not numbers:
        return None
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return {
        "total": total,
        "count": count,
        "average": average,
        "min": min(numbers),
        "max": max(numbers)
    }

def create_person(**kwargs):
    """Create a person dictionary from keyword arguments."""
    return kwargs

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

# Lambda functions (anonymous functions)
square = lambda x: x**2
is_even = lambda x: x % 2 == 0

def main():
    """Demonstrate various function examples."""
    print("=== Functions in Python ===\n")
    
    # Simple function
    print(greet("Alice"))
    print(greet("Bob"))
    print()
    
    # Function with multiple parameters
    print(f"5 + 3 = {add(5, 3)}")
    print()
    
    # Default parameters
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"multiply(5) = {multiply(5)}")
    print()
    
    # Variable arguments
    stats = calculate_stats(10, 20, 30, 40, 50)
    print("Statistics for [10, 20, 30, 40, 50]:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    print()
    
    # Keyword arguments
    person = create_person(name="Charlie", age=25, city="Boston")
    print(f"Person: {person}")
    print()
    
    # Fibonacci
    print(f"Fibonacci(10): {fibonacci(10)}")
    print()
    
    # Lambda functions
    print(f"square(5) = {square(5)}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_even(7) = {is_even(7)}")

if __name__ == "__main__":
    main()
