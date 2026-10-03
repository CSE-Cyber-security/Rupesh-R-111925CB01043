# Factorial Program (Python)

## Description

This program calculates the **factorial** of a number entered by the user. It uses `if / elif / else` statements to handle three cases: negative numbers, zero, and positive numbers. The factorial is calculated using a simple `for` loop.

## Formula

The factorial of a non-negative integer `n` is defined as:

```
n! = n × (n-1) × (n-2) × ... × 2 × 1
```

Special case:

```
0! = 1
```

Factorial is **not defined** for negative numbers.

## Source Code

```python
n = int(input("Enter a number: "))

if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("Factorial of 0 is 1")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial of", n, "is", fact)
```

(Also available separately in `factorial_code.txt`.)

## Sample Test Cases

| S.No | Input (n) | Expected Output |
|------|-----------|-----------------|
| 1 | 5 | Factorial of 5 is 120 |
| 2 | 0 | Factorial of 0 is 1 |
| 3 | -3 | Factorial does not exist for negative numbers |
| 4 | 1 | Factorial of 1 is 1 |
| 5 | 7 | Factorial of 7 is 5040 |

## How to Run

1. Make sure Python 3 is installed on your system.
2. Copy the code from `factorial_code.txt` into a new file named `factorial.py` (or use any filename ending in `.py`).
3. Open a terminal / command prompt in that folder.
4. Run the program using:

   ```
   python factorial.py
   ```

5. Enter a number when prompted and press Enter.
6. The factorial (or an error message for negative input) will be displayed.

## Files in This Package

- `factorial_code.txt` — source code (plain text)
- `data.txt` — sample input data and expected outputs
- `screenshots/` — screenshots of the program running
- `README.md` — project documentation
