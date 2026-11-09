"""
Daily Expense Tracker
---------------------
A simple command-line program to record, view and summarise daily expenses.
Data is saved in a CSV file (expenses.csv), so it is not lost when the
program closes.

Author : Rupesh Rakesh
Python : 3.8 or newer (no external libraries needed)
"""

import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"
FIELDS = ["id", "date", "category", "description", "amount"]
CATEGORIES = ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"]


# ---------------------------------------------------------------- file handling
def load_expenses():
    """Read all expenses from the CSV file and return them as a list of dicts."""
    expenses = []
    if not os.path.exists(DATA_FILE):
        return expenses
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["id"] = int(row["id"])
            row["amount"] = float(row["amount"])
            expenses.append(row)
    return expenses


def save_expenses(expenses):
    """Write the full list of expenses back to the CSV file."""
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def next_id(expenses):
    """Give every new expense a unique number."""
    return max((e["id"] for e in expenses), default=0) + 1


# ---------------------------------------------------------------- input helpers
def ask_amount():
    """Keep asking until the user types a valid positive number."""
    while True:
        text = input("Amount (Rs.): ").strip()
        try:
            amount = float(text)
            if amount <= 0:
                print("  Amount must be greater than 0. Try again.")
                continue
            return round(amount, 2)
        except ValueError:
            print("  Please enter a number, e.g. 150 or 99.50")


def ask_category():
    """Show the category list and return the chosen one."""
    print("Categories:")
    for i, name in enumerate(CATEGORIES, start=1):
        print(f"  {i}. {name}")
    while True:
        choice = input("Choose category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print(f"  Please enter a number between 1 and {len(CATEGORIES)}.")


def ask_date():
    """Ask for a date (YYYY-MM-DD). Pressing Enter uses today's date."""
    while True:
        text = input("Date YYYY-MM-DD (press Enter for today): ").strip()
        if text == "":
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("  Wrong format. Example: 2026-11-09")


# ---------------------------------------------------------------- features
def add_expense(expenses):
    print("\n--- Add New Expense ---")
    date = ask_date()
    category = ask_category()
    description = input("Description: ").strip() or "-"
    amount = ask_amount()
    expenses.append({
        "id": next_id(expenses),
        "date": date,
        "category": category,
        "description": description,
        "amount": amount,
    })
    save_expenses(expenses)
    print("Expense added successfully!")


def print_table(rows):
    """Print a list of expenses as a neat table."""
    if not rows:
        print("No expenses found.")
        return
    print(f"{'ID':<4} {'Date':<11} {'Category':<14} {'Description':<22} {'Amount':>10}")
    print("-" * 65)
    for e in rows:
        print(f"{e['id']:<4} {e['date']:<11} {e['category']:<14} "
              f"{e['description'][:21]:<22} {e['amount']:>10.2f}")
    print("-" * 65)
    print(f"{'Total':<53} {sum(e['amount'] for e in rows):>10.2f}")


def view_all(expenses):
    print("\n--- All Expenses ---")
    print_table(sorted(expenses, key=lambda e: (e["date"], e["id"])))


def view_by_date(expenses):
    print("\n--- Expenses for a Date ---")
    date = ask_date()
    print_table([e for e in expenses if e["date"] == date])


def category_summary(expenses):
    print("\n--- Category-wise Summary ---")
    if not expenses:
        print("No expenses found.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    grand = sum(totals.values())
    print(f"{'Category':<14} {'Total':>10} {'Share':>8}")
    print("-" * 34)
    for cat, amt in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{cat:<14} {amt:>10.2f} {amt / grand * 100:>7.1f}%")
    print("-" * 34)
    print(f"{'Grand Total':<14} {grand:>10.2f}")


def monthly_summary(expenses):
    print("\n--- Monthly Summary ---")
    if not expenses:
        print("No expenses found.")
        return
    months = {}
    for e in expenses:
        key = e["date"][:7]  # YYYY-MM
        months[key] = months.get(key, 0) + e["amount"]
    for month in sorted(months):
        print(f"{month} : Rs. {months[month]:.2f}")


def delete_expense(expenses):
    print("\n--- Delete an Expense ---")
    if not expenses:
        print("No expenses to delete.")
        return
    text = input("Enter the ID to delete: ").strip()
    if not text.isdigit():
        print("Invalid ID.")
        return
    target = int(text)
    for e in expenses:
        if e["id"] == target:
            expenses.remove(e)
            save_expenses(expenses)
            print("Expense deleted.")
            return
    print("No expense with that ID.")


# ---------------------------------------------------------------- main menu
def main():
    expenses = load_expenses()
    menu = """
=========== DAILY EXPENSE TRACKER ===========
1. Add expense
2. View all expenses
3. View expenses by date
4. Category-wise summary
5. Monthly summary
6. Delete an expense
7. Exit
=============================================="""
    while True:
        print(menu)
        choice = input("Enter your choice (1-7): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_all(expenses)
        elif choice == "3":
            view_by_date(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            monthly_summary(expenses)
        elif choice == "6":
            delete_expense(expenses)
        elif choice == "7":
            print("Thank you! Your data is saved in", DATA_FILE)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
