# CSC2107 Assignment 5.1: Fibonacci Algorithms

## Group Members

- Isaac Isota (M25B23/043)
- Teta Nadine Tracy (S25B23/010)
- Nyakecho Karen Faith (M25B23/020)
- Ainebyona Sheba (M25B23/002)
- Precious Abangira Nimmusiima (M24B23/028)

## About the Assignment

This assignment compares two ways of calculating Fibonacci numbers:

- **Algorithm A:** Uses plain recursion.
- **Algorithm B:** Uses recursion with memoization to store answers that have already been calculated.

The program checks that both algorithms return the same answers for values from 0 to 20. It then measures their function calls and execution times for different values of `n`, and plots the number of calls.

## Requirements

- Python 3
- Matplotlib

Install Matplotlib if it is not already installed:

```bash
pip install matplotlib
```

## How to Run

1. Save the Python code in a file, for example `Fibonacci_Algorithm_Comparison.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python Fibonacci_Algorithm_Comparison.py
```

The program prints the experiment results and displays graphs comparing the number of function calls.

## Part 4: Testing n = 1000

The program also tests memoized recursion with `n = 1000`, tries increasing Python's recursion limit, and uses an iterative version as another way to calculate the result.

## Files

- `Fibonacci_Algorithm_Comparison.py` - Python implementation and experiments.
- `README.md` - Instructions and a short description of the assignment.

