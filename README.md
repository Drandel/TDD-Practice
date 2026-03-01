# TDD Practice

A collection of TDD kata projects using Python and pytest. Each project contains an empty class stub and a full test suite — implement the class until all tests pass.

---

## Setup

### Prerequisites

Download and install Python 3 from [python.org](https://www.python.org/downloads/) if you don't already have it.

Verify your installation by opening a terminal and running:

```bash
python --version
pip --version
```

Both commands should return a version number.

---

### 1. Install the Python Extension in VS Code

1. Open VS Code
2. Press `Ctrl+Shift+X` to open the Extensions panel
3. Search for **Python** and install the extension published by **Microsoft**
4. Reload VS Code if prompted

---

### 2. Select Your Python Interpreter

1. Open this project folder in VS Code
2. Press `Ctrl+Shift+P` to open the command palette
3. Type **Python: Select Interpreter** and select it
4. Choose the Python 3 entry from the list

---

### 3. Install Pytest

In your terminal, run:

```bash
pip install pytest
```

---

### 4. Enable the Testing Panel in VS Code

1. Press `Ctrl+Shift+P` to open the command palette
2. Type **Python: Configure Tests** and select it
3. Select **pytest**
4. Select **`. (root directory)`** as the test directory

This enables the **Testing** sidebar (beaker icon on the left) where you can run and debug tests with one click.

---

## Running Tests

From inside a project folder, run all tests with:

```bash
python -m pytest test_projectX.py -v
```

Or use the VS Code Testing panel to run and debug individual tests.

---

## Projects

| Project | Description |
|---------|-------------|
| `project1/` | Project 1 |
| `project2/` | Project 2 |
| `project3/` | Project 3 |
| `project4/` | Project 4 |
| `project5/` | Project 5 |

Each project folder contains:
- `projectX.py` — the class stub you will implement
- `test_projectX.py` — the test suite to make pass
