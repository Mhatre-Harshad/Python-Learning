# A Simple Calculator Program (Using Conditional Statements)
# Display 
print("Welcome to the Python Calculator")
print("Select an operation to perform:")
print("Addition (+)")
print("Subtraction (-)")
print("Multiplication (*)")
print("Division (/)")

#taking operator
op = input("Enter  a Operator : ")

#input
number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))

if op == '+':
    result = number1 + number2
    print(f"The sum of {number1} and {number2} is {result}")

elif op == '-':
    result = number1 - number2
    print(f"The difference between {number1} and {number2} is {result}")

elif op == '*':
    result = number1 * number2
    print(f"The product of {number1} and {number2} is {result}")

elif op == '/':
    # Handling division by zero
    if number2 != 0:
        result = number1 / number2
        print(f"The division of {number1} by {number2} is {result}")
    else:
        print("Cannot divide by zero")

else:
    print(f"{op} is an invalid operator")
