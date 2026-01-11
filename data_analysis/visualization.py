#!/usr/bin/env python3
"""
Data Visualization with Matplotlib
This demonstrates creating various plots using Matplotlib.

Note: Run 'pip install -r requirements.txt' to install dependencies before running this script.
"""

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Required libraries not installed. Please run: pip install -r requirements.txt")
    exit(1)

def line_plot():
    """Create a simple line plot."""
    print("Creating line plot...")
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.plot(x, np.cos(x), label='cos(x)', color='red', linewidth=2)
    
    plt.title('Sine and Cosine Functions', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('/tmp/line_plot.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Saved: /tmp/line_plot.png\n")

def bar_chart():
    """Create a bar chart."""
    print("Creating bar chart...")
    
    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    values = [65000, 72000, 68000, 75000]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:,.0f}',
                ha='center', va='bottom', fontsize=10)
    
    plt.title('Quarterly Sales Revenue', fontsize=16)
    plt.xlabel('Quarter', fontsize=12)
    plt.ylabel('Revenue ($)', fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('/tmp/bar_chart.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Saved: /tmp/bar_chart.png\n")

def scatter_plot():
    """Create a scatter plot."""
    print("Creating scatter plot...")
    
    # Generate sample data
    np.random.seed(42)
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.6, c=y, cmap='viridis', s=50)
    
    # Add trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')
    
    plt.colorbar(label='Y value')
    plt.title('Scatter Plot with Trend Line', fontsize=16)
    plt.xlabel('X', fontsize=12)
    plt.ylabel('Y', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.savefig('/tmp/scatter_plot.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Saved: /tmp/scatter_plot.png\n")

def multiple_subplots():
    """Create multiple subplots."""
    print("Creating multiple subplots...")
    
    x = np.linspace(0, 10, 100)
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Subplot 1: Sine
    axes[0, 0].plot(x, np.sin(x), 'b-')
    axes[0, 0].set_title('Sine Wave')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Subplot 2: Cosine
    axes[0, 1].plot(x, np.cos(x), 'r-')
    axes[0, 1].set_title('Cosine Wave')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Subplot 3: Exponential
    axes[1, 0].plot(x, np.exp(x/5), 'g-')
    axes[1, 0].set_title('Exponential Growth')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Subplot 4: Histogram
    data = np.random.randn(1000)
    axes[1, 1].hist(data, bins=30, edgecolor='black', alpha=0.7)
    axes[1, 1].set_title('Normal Distribution')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/tmp/subplots.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Saved: /tmp/subplots.png\n")

def pie_chart():
    """Create a pie chart."""
    print("Creating pie chart...")
    
    categories = ['Product A', 'Product B', 'Product C', 'Product D']
    sizes = [30, 25, 20, 25]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    explode = (0.1, 0, 0, 0)  # Explode first slice
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=categories, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Product Sales Distribution', fontsize=16)
    plt.axis('equal')
    
    plt.savefig('/tmp/pie_chart.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Saved: /tmp/pie_chart.png\n")

def main():
    """Run all visualization examples."""
    print("=== Data Visualization with Matplotlib ===")
    print("Creating various plots...\n")
    
    line_plot()
    bar_chart()
    scatter_plot()
    multiple_subplots()
    pie_chart()
    
    print("All plots have been saved to /tmp/")
    print("\nNote: In a Jupyter notebook, plots would display inline.")
    print("Run 'plt.show()' instead of 'plt.savefig()' to display plots interactively.")

if __name__ == "__main__":
    main()
