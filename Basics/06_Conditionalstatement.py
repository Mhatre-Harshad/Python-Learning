# -------------------------------------------------------------------------------------
# Condition Statements in Python
# -------------------------------------------------------------------------------------
# Conditional statements allow your program to make decisions based on conditions.
"""
Decision-making is one of the most important parts of any programming language.
It allows us to run a specific block of code when a certain condition is met.
Condition checking is the backbone of decision-making.
"""
# -------------------------------------------------------------------------------------
# Indentation
# -------------------------------------------------------------------------------------
# While coding in Python, indentation is extremely important.
# Python uses indentation to define blocks of code inside conditional statements.
# All statements inside the same block must have the same level of indentation.

# -------------------------------------------------------------------------------------
# if Statement
# -------------------------------------------------------------------------------------
# The 'if' statement executes a block of code only when the given condition is True.
"""
The if statement checks a condition (an expression that results in True or False).
If the condition is True, the block inside 'if' runs.
If the condition is False, the block is skipped.
"""

# Using if
age = 21
if age >= 18:
    print("You are able to vote")

# Multiple statements inside an if block
age = 20
if age >= 18:
    print("You are able to Vote")
    print("You are an Adult")   # You can have multiple statements inside an if block

# -------------------------------------------------------------------------------------
# if-else Statement
# -------------------------------------------------------------------------------------
# The else statement runs when the if condition evaluates to False.

"""
The if-else statement gives us two paths:
If the condition is True : run the 'if' block.
If the condition is False : run the 'else' block.
"""

# Using if-else
a = 210
b = 64
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# -------------------------------------------------------------------------------------
# elif Statement
# -------------------------------------------------------------------------------------
# The 'elif' keyword allows us to check multiple conditions one after another.

"""
The elif statement helps check several conditions.
Only the first True condition block will run.
Using elif is optional, and you can have many elif conditions as needed.
"""

# Using elif Statement
number = 100
if number == 10:
    print("number is equal to 10")
elif number == 50:
    print("number is equal to 50")
elif number == 100:
    print("number is equal to 100")
else:
    print("number is not equal to 10, 50 or 100")

# -------------------------------------------------------------------------------------
# if-elif-else Statement
# -------------------------------------------------------------------------------------
# All three keywords (if, elif, else) can be combined for multi-level decision making.
# if   : checks the first condition.
# elif : checks another condition if the previous was False.
# else : runs if none of the conditions are True.

# Using if-elif-else
a = 10
b = 20
c = 15

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

# -------------------------------------------------------------------------------------
# Nested if Statements
# -------------------------------------------------------------------------------------
# An if statement inside another if statement is called a nested if.

# Using Nested if
num = 10
if num > 0:
    print("The Number is Positive")
    if num % 2 == 0:
        print("The Number is Even")

# -------------------------------------------------------------------------------------
# Ternary Operator (Short-Hand If-Else)
# -------------------------------------------------------------------------------------
# A ternary operator lets you write a quick one-line if-else expression.

# Using short-hand if-else
a = 2
b = 33
print("A") if a > b else print("B")

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# Extra Examples for Conditional Statements
# -------------------------------------------------------------------------------------

# Ex 1: Login check

user = "Beast"
password = "3355"

if user == "Beast" and password == "3355":
    print("Login successful")
else:
    print("Invalid Account")
    print("Please check your user and password again")

# Ex 2: Temperature check
temp = 25
if temp > 40:
    print("It is extremely hot today")
elif temp > 30:
    print("It is hot today ")
elif temp > 20:
    print("The weather is nice.")
else:
    print("It is a cold day")
# -------------------------------------------------------------------------------------