def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"


print("=== Simple Calculator ===")
while True:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))
    print("Result:", calculate(a, b, op))

    again = input("Calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
