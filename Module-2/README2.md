# Module 2 — Simple Calculator

## 📌 Project Overview

This project is a simple command-line calculator application developed using Python.

The application allows the user to perform basic arithmetic operations through a menu-driven interface.

## ✨ Features

* Addition
* Subtraction
* Multiplication
* Division
* Division-by-zero error handling
* Invalid input handling
* Continuous calculations until the user chooses Exit

## 🛠️ Technologies Used

* Python 3

## 📂 Project Structure

```text
Module-2/
│
├── calculator.py
└── README.md
```

## ⚙️ Operations

| Choice | Operation      |
| ------ | -------------- |
| 1      | Addition       |
| 2      | Subtraction    |
| 3      | Multiplication |
| 4      | Division       |
| 5      | Exit           |

## ▶️ How to Run

Make sure Python 3 is installed on your system.

Open a terminal inside the `Module-2` folder and run:

```bash
python calculator.py
```

## 💻 Sample Output

```text
'' Calculator ''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter the choice 1
Enter first number: 34
Enter second number: 2
Result: 36.0

'' Calculator ''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter the choice 5
Good Bye
```

## 🧠 Python Concepts Used

* Functions
* `while` loop
* `if`, `elif`, and `else`
* Lists
* User input using `input()`
* Type conversion using `int()` and `float()`
* `try-except` exception handling
* `break`
* `continue`

## 🔐 Error Handling

The application handles invalid numerical input using `try-except`.

It also prevents division by zero:

```python
if num2 == 0:
    print("Error: Cannot divide by zero!")
```

## 🎯 Purpose

This project was developed as **Module 2** of the AI-ML Internship to practice fundamental Python programming concepts and exception handling.
