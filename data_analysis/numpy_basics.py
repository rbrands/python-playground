#!/usr/bin/env python3
"""
Introduction to NumPy
This demonstrates basic NumPy array operations.

Note: Run 'pip install -r requirements.txt' to install dependencies before running this script.
"""

try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Please run: pip install -r requirements.txt")
    exit(1)

def basic_arrays():
    """Demonstrate basic NumPy array creation and operations."""
    print("=== Basic NumPy Arrays ===\n")
    
    # Create arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr1}")
    print(f"Type: {type(arr1)}")
    print(f"Shape: {arr1.shape}")
    print(f"Data type: {arr1.dtype}\n")
    
    # 2D array
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr2d}")
    print(f"Shape: {arr2d.shape}\n")
    
    # Array creation functions
    zeros = np.zeros((2, 3))
    print(f"Zeros:\n{zeros}\n")
    
    ones = np.ones((3, 2))
    print(f"Ones:\n{ones}\n")
    
    range_arr = np.arange(0, 10, 2)
    print(f"Range (0 to 10, step 2): {range_arr}\n")
    
    linspace = np.linspace(0, 1, 5)
    print(f"Linspace (5 numbers from 0 to 1): {linspace}\n")

def array_operations():
    """Demonstrate array operations."""
    print("=== Array Operations ===\n")
    
    arr = np.array([1, 2, 3, 4, 5])
    
    # Arithmetic operations
    print(f"Original: {arr}")
    print(f"Add 10: {arr + 10}")
    print(f"Multiply by 2: {arr * 2}")
    print(f"Square: {arr ** 2}\n")
    
    # Element-wise operations
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")
    print(f"arr1 + arr2: {arr1 + arr2}")
    print(f"arr1 * arr2: {arr1 * arr2}\n")

def array_statistics():
    """Demonstrate statistical functions."""
    print("=== Array Statistics ===\n")
    
    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    
    print(f"Data: {data}")
    print(f"Mean: {np.mean(data)}")
    print(f"Median: {np.median(data)}")
    print(f"Standard Deviation: {np.std(data):.2f}")
    print(f"Min: {np.min(data)}")
    print(f"Max: {np.max(data)}")
    print(f"Sum: {np.sum(data)}\n")

def array_indexing():
    """Demonstrate array indexing and slicing."""
    print("=== Array Indexing and Slicing ===\n")
    
    arr = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr}")
    print(f"First element: {arr[0]}")
    print(f"Last element: {arr[-1]}")
    print(f"Slice [1:4]: {arr[1:4]}")
    print(f"Every other element: {arr[::2]}\n")
    
    # Boolean indexing
    print(f"Elements > 30: {arr[arr > 30]}")
    print(f"Even elements: {arr[arr % 2 == 0]}\n")

def main():
    """Run all NumPy demonstrations."""
    print("=== Introduction to NumPy ===")
    print("NumPy is the fundamental package for numerical computing in Python.\n")
    
    basic_arrays()
    array_operations()
    array_statistics()
    array_indexing()

if __name__ == "__main__":
    main()
