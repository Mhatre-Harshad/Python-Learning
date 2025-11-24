# input function is use to take input from the user
# Basic examples of using the input() function in Python

#1 Taking simple text input
name = input("Enter your name: ")
print("Hello,", name)

#2 Taking numeric input (type casting)
age = int(input("Enter your age: "))
print("You Age  is ",age,".")

#3 Taking float input
height = float(input("Enter your height in cm: "))
print("Your height is:", height, "cm")

#4 Taking multiple inputs in one line
city, country = input("Enter your city and country with space  ").split()
print("You live in:", city, country)
#----------------------------------------------------------------------
"""F-string: A formatted string literal that lets you embed 
variables or expressions inside {} using the prefix 'f'."""

#1 Simple f-string example
student = "Harshad"
print(f"Student name is {student}")

#2  with numbers
marks = 100
print(f"Marks scored: {marks}")

#3 with expressions
a = 14
b = 59
print(f"The sum of {a} and {b} is {a + b}")

#4 f-string showing formatted float
price = 75.567
print(f"Rounded price: {price:.2f}")

#5  with multiple variables
language = "Python"
version = 3.12
print(f"I am learning {language} language  version {version}")
