# input_function_demo.py
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
city, country = input("Enter your city and country  ").split()
print("You live in:", city, country)


