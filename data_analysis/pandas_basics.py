#!/usr/bin/env python3
"""
Introduction to Pandas
This demonstrates basic Pandas DataFrame operations.

Note: Run 'pip install -r requirements.txt' to install dependencies before running this script.
"""

try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Required libraries not installed. Please run: pip install -r requirements.txt")
    exit(1)

def create_dataframes():
    """Demonstrate DataFrame creation."""
    print("=== Creating DataFrames ===\n")
    
    # From dictionary
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'city': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
        'salary': [70000, 85000, 95000, 72000, 88000]
    }
    df = pd.DataFrame(data)
    print("DataFrame from dictionary:")
    print(df)
    print(f"\nShape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}\n")
    
    return df

def basic_operations(df):
    """Demonstrate basic DataFrame operations."""
    print("=== Basic Operations ===\n")
    
    # View first/last rows
    print("First 3 rows:")
    print(df.head(3))
    print()
    
    # Info about DataFrame
    print("DataFrame Info:")
    print(df.info())
    print()
    
    # Describe statistics
    print("Statistical Summary:")
    print(df.describe())
    print()

def selecting_data(df):
    """Demonstrate data selection."""
    print("=== Selecting Data ===\n")
    
    # Select a column
    print("Names column:")
    print(df['name'])
    print()
    
    # Select multiple columns
    print("Name and age:")
    print(df[['name', 'age']])
    print()
    
    # Select rows by index
    print("First row:")
    print(df.iloc[0])
    print()
    
    # Select rows by condition
    print("People older than 30:")
    print(df[df['age'] > 30])
    print()

def data_manipulation(df):
    """Demonstrate data manipulation."""
    print("=== Data Manipulation ===\n")
    
    # Add a new column
    df_copy = df.copy()
    df_copy['bonus'] = df_copy['salary'] * 0.1
    print("DataFrame with bonus column:")
    print(df_copy)
    print()
    
    # Sort data
    sorted_df = df.sort_values('salary', ascending=False)
    print("Sorted by salary (descending):")
    print(sorted_df)
    print()
    
    # Group by and aggregate
    print("Average salary:")
    print(f"${df['salary'].mean():,.2f}")
    print()

def working_with_data():
    """Demonstrate creating and analyzing data."""
    print("=== Working with Sample Data ===\n")
    
    # Create sample sales data
    dates = pd.date_range('2024-01-01', periods=12, freq='ME')
    sales_data = {
        'month': dates,
        'revenue': [50000, 52000, 48000, 55000, 58000, 62000,
                   65000, 61000, 59000, 63000, 68000, 72000],
        'expenses': [30000, 31000, 29000, 32000, 33000, 35000,
                    36000, 34000, 33000, 35000, 37000, 38000]
    }
    
    sales_df = pd.DataFrame(sales_data)
    sales_df['profit'] = sales_df['revenue'] - sales_df['expenses']
    sales_df['profit_margin'] = (sales_df['profit'] / sales_df['revenue'] * 100).round(2)
    
    print("Monthly Sales Data:")
    print(sales_df)
    print()
    
    print("Summary Statistics:")
    print(f"Total Revenue: ${sales_df['revenue'].sum():,}")
    print(f"Total Expenses: ${sales_df['expenses'].sum():,}")
    print(f"Total Profit: ${sales_df['profit'].sum():,}")
    print(f"Average Profit Margin: {sales_df['profit_margin'].mean():.2f}%")
    print()

def main():
    """Run all Pandas demonstrations."""
    print("=== Introduction to Pandas ===")
    print("Pandas is a powerful data manipulation and analysis library.\n")
    
    df = create_dataframes()
    basic_operations(df)
    selecting_data(df)
    data_manipulation(df)
    working_with_data()

if __name__ == "__main__":
    main()
