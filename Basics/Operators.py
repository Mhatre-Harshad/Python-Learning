# ---------------------------------------------
# Operators
# ---------------------------------------------
# Operators  are used to perform operations on values and variables
# There are 7 types of operator in python


# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform  mathematical operations
a = 10
b = 3

print("Addition:",a + b)        # Adds two values
print("Subtraction:",a - b)     # Subtracts two values
print("Multiplication:",a * b)  # Multiplies two values
print("Division:",a / b)        # Divides two values and returns float( i.e decimal value)
print("Floor Division:",a // b) # Divides two values and returns integer (rounds the decimal value to its nearest integer)
print("Modulus:",a % b)         # Divides two values and returns the remainder
print("Power:",a ** b)          # raises x to power of y (eg: 2**3 = 2x2x2)
#--------------------------------------------------------------------------
# Assignment Operators
# Assignment operators are used to assign values to variables.

num =10
num += 5  # add and assign / same as num=num+5  /add 5 to val assign it to varaible num

print("+=:", num)

num -=3  # subtract and assign  /same as num =num-3  / subtract 3 from val assign it to varaible num
print("-= :", num)

num *= 2  # multiply and assign   /multiply val by 2 and assign it to varaible num
print("*= :", num)

num /=2  # divide and assign    /divide val by 2 and assign it to varaible num
print("/= :", num)
#--------------------------------------------------------------------------
# Comparison Operators
# Comparison operators are used to compare two values and return True/False

a = 5
b = 8
print("Equal to ", a == b)
print("Not Equal to", a != b)
print("Greater than", a > b)
print("Less than?", a < b)
print(" Greater than or equal to", a >= b)
print("Less than or equal to", a <= b)

#--------------------------------------------------------------------------
#Logical Operators
# Logical operators are used to combine conditional statements

age = 20
student = True

# logical and → both conditions must be true
print("Adult AND Student:", age >= 18 and student)

# logical or → at least one condition must be true
print("Adult OR Student:", age <= 18 or student)

# logical not → reverses the condition 
print("Not  student:", not student)
#--------------------------------------------------------------------------
# Membership Operators
#Membership operators are used to test if a sequence is presented in an object like list string, etc
#in      :    Returns true if value is found in the sequence
#not in  :    Returns true if value is not found in the sequence
fruit = ["apple", "banana", "mango"]

print("mango" in fruit)
print("grapes" not in fruit)

#--------------------------------------------------------------------------
#Identity Operators
# Check if two variables are actually the same object.
"""Identity operators are used to compare the objects,
   not if they are equal, but if they are actually the same object,
   with the same memory location        """

a = [1, 2, 3]
b = a
c = [1, 2, 3]
#is      :   Returns true if the operands are identical 
#is not  :  Returns true if the operands are not identical
print( a is b)   # (same object)
print( a is c)   # (same content, but different objects)
print(a == c)   # (compares values)
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
print(a is not c) 
#--------------------------------------------------------------------------
#Bitwise Operator
#Bitwise operators are used to compare (binary) numbers
m = 6   # 110 in binary
n = 3   # 011 in binary

print("Bitwise AND (&):", m & n)   # Sets each bit to 1 if both bits are 1
print("Bitwise OR (|):", m | n)    # Sets each bit to 1 if one of two bits is 1
print("Bitwise XOR (^):", m ^ n)   # Sets each bit to 1 if only one of two bits is 1
print("Bitwise NOT (~):", ~m)      # Flips bits /Inverts all the bits
print("Left Shift :", m << 1)# Shift left by pushing zeros in from the right and let the leftmost bits fall off  """
print("Right Shift :", m >> 1)#Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
#--------------------------------------------------------------------------