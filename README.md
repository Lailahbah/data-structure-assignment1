
# Stack-Based Mathematical Expression Calculator

## 1. Project Overview

This project is a Python-based mathematical expression calculator developed for the Data Structures and Algorithm Analysis module.

The program uses the Stack data structure to evaluate mathematical expressions while respecting operator precedence and parentheses.

Mathematical expressions are read from an input file named `input.txt`. The program evaluates each expression and writes the corresponding results to `output.txt`.

The project demonstrates the practical application of stacks, algorithms, file handling, and error management in Python programming.

## 2. Project Objectives

The main objectives of this project are:

- To implement a Stack data structure using Python.
- To demonstrate the Last-In, First-Out (LIFO) principle.
- To evaluate mathematical expressions using stacks.
- To apply operator precedence correctly.
- To support parentheses and nested expressions.
- To read expressions from an external text file.
- To save calculated results in an output file.
- To identify and report invalid mathematical expressions.

## 3. Features

The calculator supports:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Operator precedence
- Parentheses and nested parentheses
- Decimal calculations
- Multiple expressions in one input file
- Error handling for invalid expressions
- Automatic generation of output results

The current version expects spaces between numbers and operators. Parentheses may be attached to numbers.

## 4. Project Structure

The project contains four main files:

    stack calculator/
    |
    |-- calculator.py
    |-- input.txt
    |-- output.txt
    |-- README.md

### calculator.py
Contains the Python source code implementing the stack, expression evaluation, and file processing.

### input.txt
Contains mathematical expressions to be evaluated, with one expression per line.

### output.txt
Stores calculated results and error messages separated by dashed lines.

### README.md
Provides instructions and documentation explaining the project.

## 5. Data Structure Used

The main data structure used in this project is the Stack.

A Stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element inserted is the first element removed.

The following stack operations are implemented:

- push(): Adds an element to the stack.
- pop(): Removes and returns the top element.
- peek(): Returns the top element without removing it.
- is_empty(): Checks whether the stack contains any elements.

The calculator uses two stacks:

1. Values Stack: Stores mathematical operands.
2. Operators Stack: Stores arithmetic operators and parentheses.

These stacks allow mathematical expressions to be evaluated according to operator precedence.

## 6. Program Design and Functions

### Stack Class
Implements the Stack data structure using a Python list.

### precedence(operator)
Determines the priority of arithmetic operators.

Multiplication and division have higher precedence than addition and subtraction.

### apply_operator(a, b, operator)
Performs an arithmetic operation using two operands.

It also checks for division by zero.

### evaluate_expression(expression)
Processes mathematical expressions using two stacks.

The function handles parentheses, operator precedence, mathematical operations, and invalid expressions.

### process_file()
Reads mathematical expressions from `input.txt`, evaluates them, and writes the results into `output.txt`.

## 7. How to Run the Program

### Requirements

- Python 3 installed on the computer.
- Visual Studio Code or another suitable code editor.

### Instructions

Step 1: Open the project folder in Visual Studio Code.

Step 2: Ensure all four project files are in the same folder.

Step 3: Open `input.txt` and enter mathematical expressions.

Step 4: Save the input file.

Step 5: Open the VS Code terminal in the project folder.

Step 6: Run the following command:

    python calculator.py

Step 7: Open `output.txt` to view the results.

The terminal displays:

    Results written to output.txt

## 8. Sample Input

Example expressions in `input.txt`:

    3 + 5 * 2
    (8 / 4) + 7 * 2
    10 - (2 + 3) * 4
    20 / 5 * 2
    2 * (3 + (4 * 5))
    10 / 0
    (3 + 2
    10 / 4
    3 + 2)
    3 +

## 9. Sample Output

The corresponding results in `output.txt` are:

    13
    -----
    16
    -----
    -10
    -----
    8
    -----
    46
    -----
    Error: Division by zero
    -----
    Error: Unmatched (
    -----
    2.5
    -----
    Error: Unmatched )
    -----
    Error: Missing operand

## 10. Testing and Results

The calculator was tested using ten mathematical expressions covering normal operations and selected error conditions.

The tests verified:

- Correct arithmetic operations.
- Operator precedence.
- Nested parentheses.
- Decimal division.
- Division-by-zero handling.
- Detection of unmatched parentheses.
- Detection of missing operands.
- Successful reading and writing of text files.

All ten selected test cases produced their expected results.

## 11. Known Limitations

The current implementation expects operators to be separated by spaces.

It does not fully support unary negative numbers or implicit multiplication.

For example, an expression such as `2(3 + 4)` is not supported.

Blank lines in `input.txt` may produce an invalid-expression error.

These limitations could be addressed through improved tokenization and input validation.

## 12. Conclusion

This project demonstrates how the Stack data structure can be applied to solve mathematical expressions efficiently.

By combining stack operations, operator precedence, parentheses handling, and file processing, the program provides a practical example of data structures and algorithm design.

The successful execution of the selected test cases demonstrates that the core calculator functions operate correctly for the supported inputs.
