#Performs +, -, *, / based on user input.

# Get first number from user
x = float(input("Input first number: "))
# Get second number from user
y = float(input("Input second number: "))
# Get operation from user
op = input("Input operation (+, -, *, /): ")

if op == '+':
    print(f"Result: {x + y}")
elif op == '-':
    print(f"Result: {x - y}")
elif op == '*':
    print(f"Result: {x * y}")
elif op == '/':
    if y != 0:
        print(f"Result: {x / y}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation.")

