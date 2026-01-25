# Python Playground

A comprehensive Python learning environment that takes you from "Hello World" to data analysis. This repository contains practical examples organized by difficulty level, perfect for learning Python or experimenting with new concepts.
For further learning see the book [Python for Data Analysis](https://wesmckinney.com/book/) from Wes McKinney

## 📚 Contents

### 🌱 Basics
Start your Python journey with fundamental concepts:
- **hello_world.py** - Your first Python program
- **variables_and_types.py** - Data types, variables, lists, dictionaries, and more
- **control_flow.py** - If statements, loops, and list comprehensions

### 🚀 Intermediate
Build on the basics with more advanced topics:
- **functions.py** - Function definitions, parameters, lambda functions
- **file_operations.py** - Reading and writing text and JSON files
- **classes_and_oop.py** - Object-oriented programming with classes

### 📊 Data Analysis
Explore data science with popular libraries:
- **numpy_basics.py** - NumPy arrays and numerical operations
- **pandas_basics.py** - DataFrames and data manipulation
- **visualization.py** - Creating charts and plots with Matplotlib

### 📊 Jupyter Notebooks
Data Science with Jupyter Notebooks. The environment has been enabled to use Jupyter Notebooks.
- **example_notebook.jpynb** - Simple notebook as starter.
- **numpy_comprehensive.ipynb** - Comprehensive NumPy tutorial covering arrays, operations, linear algebra, statistics, and more
- **machine_learning_iris_flowers.ipynb** - Machine Learning with the public standard learning dataset
- **azure_blob_storage.ipynb** - Demonstrates a typical Machine Learning workflow with Azure Blob Storage
- **excel_and_csv.ipynb** - Shows how to read Excel and CSV files
- **visualization.ipynb** - Matplotlib inline plots (line, bar, scatter, subplots, pie, box, stacked area, correlation heatmap) with Pandas integration

## 🚀 Getting Started

### Option 1: GitHub Codespaces (Recommended)
The easiest way to get started is using GitHub Codespaces:

1. Click the **Code** button on the GitHub repository
2. Select **Codespaces** tab
3. Click **Create codespace on main**

The development environment will be automatically configured with Python 3.14 and all dependencies installed!

### Option 2: Local Installation

#### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

#### Installation

1. Clone the repository:
```bash
git clone https://github.com/rbrands/python-playground.git
cd python-playground
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies for data analysis examples:
```bash
pip install -r requirements.txt
```

## 💻 Running the Examples

### Basic Examples
No dependencies required - just run them:
```bash
python3 basics/hello_world.py
python3 basics/variables_and_types.py
python3 basics/control_flow.py
```

### Intermediate Examples
```bash
python3 intermediate/functions.py
python3 intermediate/file_operations.py
python3 intermediate/classes_and_oop.py
```

### Data Analysis Examples
Make sure you've installed the requirements first:
```bash
python3 data_analysis/numpy_basics.py
python3 data_analysis/pandas_basics.py
python3 data_analysis/visualization.py
```

## 📖 Learning Path

1. **Start with Basics**: Begin with `hello_world.py` and work through the basics directory
2. **Move to Intermediate**: Once comfortable, explore functions, file operations, and OOP
3. **Explore Data Analysis**: Install the requirements and dive into NumPy, Pandas, and visualization

## 🔧 What You'll Learn

- **Python Fundamentals**: Variables, data types, control flow
- **Functions**: Writing reusable code with functions
- **File I/O**: Reading and writing files
- **OOP**: Object-oriented programming concepts
- **Data Analysis**: Working with NumPy arrays and Pandas DataFrames
- **Visualization**: Creating informative charts and plots
- **Notebooks**: Working with Jupyter Notebooks

## 📦 Dependencies

For data analysis examples, the following libraries are used:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization
- **scikit-learn** - Machine Learning

All dependencies are listed in `requirements.txt`.

## 🤝 Contributing

Feel free to experiment, modify, and extend these examples! This is a playground after all.

### Pull Request Guidelines
This repository requires all changes to be submitted via Pull Requests:
- All PRs require review and approval from @rbrands
- Direct pushes to the `main` branch are not allowed
- See [Branch Protection Setup](.github/BRANCH_PROTECTION_SETUP.md) for configuration details

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Resources

### Python for Data Analysis
<img src="https://wesmckinney.com/book/images/cover.png" alt="Python for Data Analysis" width="200"/>

The comprehensive guide to data analysis with Python by Wes McKinney (creator of Pandas).
- [Python for Data Analysis - 3rd Edition](https://wesmckinney.com/book/)

### Mathematics of Machine Learning
<img src="https://camo.githubusercontent.com/d8c97bfaf2906f56e6fb726ff3ed573297e67a9a4d8fc44cf4acbbb2bf5d49cd/68747470733a2f2f636f6e74656e742e7061636b742e636f6d2f4233323130342f636f7665725f696d6167655f736d616c6c2e6a7067" alt="Mathematics of Machine Learning" width="200"/>

An open-source book covering the mathematical foundations of machine learning.
- [Mathematics of Machine Learning Book](https://github.com/cosmic-cortex/mathematics-of-machine-learning-book/blob/main/README.md)

### Numerical Python
<img src="https://jrjohansson.github.io/images/numericalpython-cover-ed3.jpg" alt="Numerical Python" width="200">

Comprehensive tutorial and reference for scientific computing with Python, NumPy, and SciPy. The modern version of the legendary "Numerical Recipes in C".
- [Numerical Python](https://jrjohansson.github.io/numericalpython.html)

## 🎯 Next Steps

After working through these examples, consider:
- Learning about web frameworks like Streamlit, Chainlit, Flask or Django
- Diving deeper into machine learning with scikit-learn
- Contributing to open-source Python projects
