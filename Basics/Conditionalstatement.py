# ------------------------------------------------------------
# Condition Statements in Python
# ------------------------------------------------------------
# Condition statements let your program make decisions.
# They check if something is true, and based on that,
# different blocks of code will run.
# ------------------------------------------------------------

#if Statement

#The if statement is used to execute a block of code only when a specified condition is true
"""The if statement evaluates a condition (an expression that results in True or False).
 If the condition is true, the code block inside the if statement is executed. 
 If the condition is false, the code block is skipped """

# Using if
age=21
if age >= 18:
    print("You are able to vote ")

#Multiple Statements in if block
# Using  Mutliple statment in if
age=20
if age >= 18:
    print("You are able to Vote ")
    print("You are an Adult ") #You can have multiple statements inside an if block
# ------------------------------------------------------------
# if-else Statement
#The if-else statement provides an alternative block of code to execute if the condition is false

# Using if-else
a = 210
b = 64
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 
# ------------------------------------------------------------
#if-elif-else Statment
# Using if-elif-else 
#if-elif-else is used to handle multiple decision paths in your program.
a = 10
b = 20
c = 15
# Compare 
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


