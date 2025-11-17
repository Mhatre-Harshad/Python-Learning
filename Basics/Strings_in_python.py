# -------------------------------------------------------------------------------------
# Python Strings
# -------------------------------------------------------------------------------------
# In Python, a string is a sequence of characters enclosed in quotes.
# Strings are used to store text such as names, messages, or any character data.
# They are immutable – meaning once created, their content cannot be modified directly.
# -------------------------------------------------------------------------------------
# Creating Strings
# -------------------------------------------------------------------------------------
name = "Harshad"
msg = 'Welcome to Python!'
multiline = """This is a
multi-line string."""

print("Name:",name)
print("Message:",msg)
print("Multi-line string\n",multiline)

# -------------------------------------------------------------------------------------
# String Concatenation (joining strings) 
# -------------------------------------------------------------------------------------
" + operator is used to add two strings"
greet = "Hello," + name
print("Concatenated String:",greet)

# -------------------------------------------------------------------------------------
#  String Length
# -------------------------------------------------------------------------------------
" len() fuction is used to find length of a string"
str= "Hello World"
print("Length of str:",len(str))

# -------------------------------------------------------------------------------------
#  Accessing Character/s of  string (Indexing)
# -------------------------------------------------------------------------------------
# Indexing allows access to individual characters in a string.
# Positive indexing starts from 0 (left → right)
# Negative indexing starts from -1 (right → left)
name="Harshad"

print("Accessing first letter:",name[0])    #H
print("Accessing second letter:",name[1])   #a
print("Accessing third letter:",name[3])    #r

print("Accessing last letter:",name[-1])    #d
print("Accessing  second last letter:",name[-2])  #a
# -------------------------------------------------------------------------------------
#  String Slicing
# -------------------------------------------------------------------------------------
"You can return a range of characters by using the slice syntax"
# substring = s[start : end : step]  <-syntax 

# Parameters:
# s: The original string.
# start (optional): Starting index (inclusive). Defaults to 0 if omitted.
# end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
# step (optional): Interval between indices. 

# Negative indexing:
# It is useful for accessing elements from the end of the String. The last element has an index of -1, the second last element -2 and so on.
"""
Positive Indexing always starts from 0

Example:
        Index:        0 1 2 3 4 5 6 7 8 9 10
        String:       H e l l o   W o r l d
                      | | | | | | | | | | |
        Text:        "Hello World"

Negative indexing also works in Python:

        Index:       -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
        String:       H   e  l  l  o     W  o  r  l  d
                      |   |  |  |  |     |  |  |  |  |
        Text:        "Hello World"

Note:
- Spaces are counted as characters.
- Positive indexes start from the left (0 → n)
- Negative indexes start from the right (-1 → -n)w
"""
string1="Hi Harshad this side"
print("\nFirst character:", string1[0])
print("Last character:", string1[-1])

text = "Data Science"
# Slice first 4 characters
print("First 4 characters:",text[:4])     #Data

# Slice from index 5 to the end
print("From index 5 to end:", text[5:])    #Science

# Slice characters from index 2 to 7
print("Characters 2 to 7:", text[2:8])     #ta Sci

# Slice using negative indexes
print("Last 3 characters:", text[-3:])     #nce

# Reverse the entire string
print("Reversed string:", text[::-1])      #ecneicS ataD

# Skip characters using step value
print("Every 2nd character:", text[::2])  # Dt cec

# -------------------------------------------------------------------------------------
# Useful String Methods
# -------------------------------------------------------------------------------------
str1 = "python programming"

print("\nString Methods:")
# Converts the entire string to uppercase 
print("Uppercase:", str1.upper())

# Converts the entire string to lowercase 
print("Lowercase:", str1.lower())

# Converts the first letter of every word to uppercase (title format)
print("Title Case:", str1.title())

# Replaces one word/substring with another
print("Replace:", str1.replace("python", "advanced python"))

# Counts how many times a specific character/substring appears
print("Count of 'p':", str1.count('p'))

# Checks if the string starts with a specific substring
print("Starts with 'py':",str1.startswith("py"))

# Checks if the string ends with a specific substring
print("Ends with 'ing':",str1.endswith("ing"))

# -------------------------------------------------------------------------------------
# Checking Content of Strings
# -------------------------------------------------------------------------------------
text = "12345"
print("\nChecking Content:")
# Returns True if all characters are digits (0–9)
print("Is digit:", text.isdigit())

# Returns True if all characters are alphabetic (A–Z or a–z)
print("Is alphabetic:", text.isalpha())

# Returns True if characters are either letters or digits (no symbols/spaces allowed)
print("Is alphanumeric:", text.isalnum())


# -------------------------------------------------------------------------------------
# Escape Characters
# -------------------------------------------------------------------------------------
# Common Escape Characters in Python
"""Escape characters are special sequences that begin with a backslash (\) 
       and tell Python to treat the next character in a special way """
# \n : New line
print("Hello\nWorld")

# \t : Tab space
print("Hello\tWorld")

# \" : Double quote inside double-quoted string (Lets you place double quotes inside a double-quoted string)
print("He said \"Python is awesome!\"")

# \' : Single quote inside single-quoted string (Lets you use a single quote inside single-quoted strings.)
print('It\'s a good day')

# \\ : Backslash (prints a single backslash)
print("C:\\Users\\Documents")



# -------------------------------------------------------------------------------------
# f-Strings (formatted strings)
# -------------------------------------------------------------------------------------
# f-strings allow embedding variables directly inside strings using {}
age = 22
print("\nUsing f-strings:")
print(f"My name is {name} and I am {age} years old.")
print(f"Reversed name: {name[::-1]}")
print(f"Length of the message is {len(msg)} characters.")

# -------------------------------------------------------------------------------------
#  String Formatting Using format() function
# -------------------------------------------------------------------------------------
name="Mhatre"
age=21
print("My name is {} and I am {} years old.".format(name, age))

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
