# Fibonacci Series in Python

A simple Python program that prints the Fibonacci series up to a number of terms entered by the user.

## What is the Fibonacci Series?

It is a series where each number is the sum of the two numbers before it, starting from 0 and 1.

```
0, 1, 1, 2, 3, 5, 8, 13, ...
```

## How the Program Works

1. The user enters how many terms they want (`n`).
2. Two variables start with the first two numbers: `a = 0` and `b = 1`.
3. A `for` loop runs `n` times. In each round:
   - It prints the current value of `a`.
   - It updates the values: `a` becomes `b`, and `b` becomes `a + b`.
4. After the loop ends, the series is complete.

## Code

```python
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series: ", end="")
for i in range(n):
    print(a, end="")
    a, b = b, a + b
print()
```

## Requirements

- Python 3.x

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   ```
2. Go to the project folder:
   ```bash
   cd <your-repo-name>
   ```
3. Run the program:
   ```bash
   python fibonacci.py
   ```

## Sample Output

```
Enter the number of terms: 7

Fibonacci Series: 0112358
```

## Concepts Used

- User input with `input()` and type conversion with `int()`
- Variables and multiple assignment (`a, b = b, a + b`)
- `for` loop with `range()`
- Printing with the `end` parameter

## Author

**Rupesh Rakesh**
Cyber Security Student, S.A. Engineering College
