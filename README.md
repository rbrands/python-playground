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
- **machine_learning_iris_flowers** - Machine Learning with the public standard learning dataset
- **azure_blob_storage.ipynb** - Demonstrates a typical Machine Learning workflow with Azure Blob Storage

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

## 📦 Dependencies

For data analysis examples, the following libraries are used:
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **matplotlib** - Data visualization

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

## 🎯 Next Steps

After working through these examples, consider:
- Exploring Jupyter notebooks for interactive analysis
- Learning about web frameworks like Flask or Django
- Diving deeper into machine learning with scikit-learn
- Contributing to open-source Python projects

Happy coding! 🐍
