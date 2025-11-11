# -------------------------------------------------------------------------------------
# Loops in Python
# -------------------------------------------------------------------------------------
# Loops are used to execute a block of code repeatedly as long as a condition is true.
# They make programs more efficient by reducing repetition and automating tasks.
# We use them to repeat tasks without rewriting code, making the program shorter, faster, and easier to manage
# -------------------------------------------------------------------------------------
"""
In programming, loops allow us to perform repetitive tasks efficiently.
Instead of writing the same code multiple times, we use loops to repeat
a block of code until a specific condition is met.

Python provides three main types of loops:
1.while loop:
Repeats a statement or group of statements while a given condition is TRUE.
It tests the condition before executing the loop body.

2.for loop:
We use for loop statements in Python to repeat a block of code for every item in a sequence like a list, string, or range.
It is best when we know how many times to loop.

3.nested loops
Python nested loops mean placing one loop inside another.
We use them when we want to repeat actions within another loop, like handling rows and columns.
"""
# -------------------------------------------------------------------------------------
# The while Loop
# -------------------------------------------------------------------------------------
# The while loop runs as long as a specified condition remains True.
# Caution : if the condition never becomes False, the loop will run forever (Infinite).

# Syntax:
#    while condition:
        #code block

# Ex 1: Basic while loop
count = 1
while count <= 7:
    print("Count:", count)
    count += 1

# Ex 2: Using while loop to calculate sum
total = 0
number = 1
while number <= 5:
    total += number
    number += 1
print("Sum of first 5 numbers:", total)

# Ex 3: using else statement
count = 1
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished")

# -------------------------------------------------------------------------------------
# The for Loop
# -------------------------------------------------------------------------------------
# The for loop is used to iterate (go through) a sequence such as a list, tuple,string, or range of numbers.

# Syntax: 
# for variable in sequence:
        # code block

# Ex 1: Iterating through a list
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)

# Ex 2: Iterating using range ()function 
# The range() function has 3 parameters : range(start,stop,step)
for i in range(5):
    print("Iteration:", i)

# Ex 3: Custom range with parameters
for number in range(1, 11, 2):
    print("Odd number:", number)

# -------------------------------------------------------------------------------------
# Nested Loops
# -------------------------------------------------------------------------------------
# A loop inside another loop is called a nested loop.

"""In Python, when you write one or more loops within a loop statement that is known as a nested loop.
 The main loop is considered as outer loop and loop(s) inside the outer loop are known as inner loops."""
# The inner loop will complete all its iterations for each iteration of the outer

for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"i={i}, j={j}")

# Ex: Printing a simple pattern
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()  # new line
  

# -------------------------------------------------------------------------------------
#Loop Control Statements
# -------------------------------------------------------------------------------------
"""We can change the normal sequence of while loop's execution using the loop control statement.
   When the while loop's execution is completed, all automatic objects defined in that scope are demolished.
   Python offers the following control statement to use within the while loop."""

# -------------------------------------------------------------------------------------
# The break Statement
# -------------------------------------------------------------------------------------

# break is used to exit the loop immediately, even if the condition is still True.
# Python break statement is used to terminate the current loop and resumes execution at the next statement.
# The break statement can be used in both Python while and for loops.
for letter in 'Python':    
   if letter == 'h':
      break
   print ("Current Letter :", letter)
print ("Good bye!")

# -------------------------------------------------------------------------------------
# The continue Statement
# -------------------------------------------------------------------------------------
# continue skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
# It helps control loop flow by ignoring specific cases without breaking the loop


for i in range(1, 10):
    if i == 5:
        continue  # Skips 5
    print("Number:", i)

# -------------------------------------------------------------------------------------
# The pass Statement
# -------------------------------------------------------------------------------------

# pass is used as a placeholder when no code needs to be executed.
# It helps maintain code structure without causing syntax errors.
# It acts as a placeholder in your code for future implementation.
# Ex 1:
for letter in "Python":
    if letter == 'h':
        pass  # only acts as a place holder for code in future use
    print("Letter:", letter)

# Ex 2: Using pass in if statement
x = 10
if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is not greater than 5")
print("Outside if")

# -------------------------------------------------------------------------------------
# The else Block with Loops
# -------------------------------------------------------------------------------------
# The 'else' clause in a loop runs only when the loop completes normally
# (i.e., without a break statement).

for number in range(3):
    print("Number:", number)
else:
    print("Loop completed successfully")

# Example with break (else won’t execute)
for number in range(3):
    if number == 2:
        break
    print("Number:", number)
else:
    print("This will not print because loop ended with break")




# -------------------------------------------------------------------------------------
# Extra Examples
# -------------------------------------------------------------------------------------

# Ex 1: Searching for an item in a list
names = ["Kartik", "Atharva", "Harsh", "Sumit"]
search = "Harsh"
for name in names:
    if name == search:
        print(f"{search} found in the list.")
        break
else:
    print(f"{search} not found in the list.")

# Ex 2: Checking even and odd numbers
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

# Ex 3: Countdown timer
import time
print("Countdown starting")
count = 5
while count > 0:
    print(count)
    time.sleep(1)
    count -= 1
print("Time up!")

# -------------------------------------------------------------------------------------
