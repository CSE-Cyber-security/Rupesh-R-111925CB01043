# Daily Expense Tracker

A simple command-line program in **Python** that helps you record your daily
spending, see where your money goes, and keep the data saved between runs.

**Author:** Rupesh Rakesh — S.A. Engineering College (Cyber Security)

---

## Features

- Add an expense (date, category, description, amount)
- View all expenses in a neat table with the total
- View expenses of one particular date
- Category-wise summary with percentage share
- Monthly summary
- Delete an expense by its ID
- Data is saved automatically in `expenses.csv`
- Input validation (wrong date, negative amount, invalid menu choice are all handled)

## Project Files

| File | Purpose |
|------|---------|
| `expense_tracker.py` | Main program |
| `output.txt` | Sample run of the program |
| `README.md` | This file |
| `expenses.csv` | Created automatically when you add your first expense |

## Requirements

- Python 3.8 or newer
- No external libraries needed (only built-in `csv`, `os`, `datetime`)

## How to Run

```bash
python expense_tracker.py
```

(On some systems use `python3 expense_tracker.py`.)

## How to Use

1. Run the program — a menu with options 1 to 7 appears.
2. Type the option number and press Enter.
3. For **Add expense**: enter the date (or press Enter for today), choose a
   category number, type a short description, then the amount.
4. Choose **Exit (7)** when done. Your data stays saved in `expenses.csv`.

## How It Works (Short Explanation)

- Every expense is stored as one row in a CSV file with the fields
  `id, date, category, description, amount`.
- When the program starts, `load_expenses()` reads the file into a list.
- Each feature (add, view, summary, delete) works on that list, and
  `save_expenses()` writes it back after any change.
- Summaries use Python dictionaries to add up amounts per category or month.

## Sample Output

See `output.txt` for a full run. A short part of it:

```
ID   Date        Category       Description                Amount
-----------------------------------------------------------------
1    2026-11-09  Food           Breakfast at canteen        45.00
2    2026-11-09  Transport      Bus pass top-up            200.00
3    2026-11-09  Shopping       Notebook and pens          120.50
-----------------------------------------------------------------
Total                                                     365.50
```

## Possible Future Improvements

- Monthly budget limit with a warning
- Edit an existing expense
- Charts using `matplotlib`
- A simple GUI or web version

---
Made as a GitHub platform task — Daily Expense Tracker.
