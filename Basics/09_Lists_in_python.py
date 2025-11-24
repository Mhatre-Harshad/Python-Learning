# -------------------------------------------------------------------------------------
# Python Lists
# -------------------------------------------------------------------------------------
# A list is a collection of items (elements) that is:
# - Ordered
# - Mutable (can be changed)
# - Allows duplicate values
# Lists are written using square brackets []
# -------------------------------------------------------------------------------------
# Creating lists
# -------------------------------------------------------------------------------------
print("\nCreating Lists :")
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]
list1 = ["Harshad", 22, 5.8, True]

print("Fruits list:", fruits)
print("Numbers list:", numbers)
print("Mixed list:", list1)

# -------------------------------------------------------------------------------------
# Accessing List Elements (Indexing)
# -------------------------------------------------------------------------------------
"""
To access values in lists, use the square brackets for slicing along with the index 
or indices to obtain value available at that index """

print("\nAccessing Elements :")

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# -------------------------------------------------------------------------------------
# Slicing Lists
# -------------------------------------------------------------------------------------
print("\nSlicing Lists :")
print("First 2 fruits:", fruits[:2])
print("Last 2 fruits:", fruits[-2:])
print("Middle numbers:", numbers[1:4])

# -------------------------------------------------------------------------------------
# Modifying List Items
# -------------------------------------------------------------------------------------
"""You can update single or multiple elements of lists by giving the slice on 
   the left-hand side of the assignment operator,
   and you can add to elements in a list with the append() method"""

print("\nModifying List Items :")
numbers = [10, 20, 30, 40, 50]
print("Before modification:", numbers)
numbers[2]="Hi"
print("After modification:", numbers)

# -------------------------------------------------------------------------------------
# Adding Items
# -------------------------------------------------------------------------------------
#Adding items to a list in Python means inserting new elements into an already existing list.
#Since lists are mutable, they can be changed after they are created. This allows you to:
# -->Add new elements
# -->Remove elements
# -->Modify elements
print("\nAdding Items :")

# -------------------------------------------------------
# 1 using append() method:
# -------------------------------------------------------
fruits = ["apple", "banana"]
print("Before append:", fruits)
fruits.append("mango")
fruits.append("orange")        # Add item at end
print("After append:", fruits)

# -------------------------------------------------------
# 2 using insert() method:
# -------------------------------------------------------
print("Before insert:", fruits)
fruits.insert(1,"papaya")       # Insert at specific position
print("After insert:", fruits)

# -------------------------------------------------------
# 3 using extend() method:
# -------------------------------------------------------
"""The extend() method in Python is used to add multiple elements from an iterable
 (such as another list) to the end of a list """
print("Before extend:", fruits)
list2=["Kiwi","Pineapple"]
print("list adding in fruits",list2)
fruits.extend(list2)
print("After extend:",fruits)
# -------------------------------------------------------------------------------------
# Removing Items
# -------------------------------------------------------------------------------------
"""Lists are ordered collections of items, and sometimes you need to remove 
   certain elements from them based on specific criteria or indices. """

print("\n Removing Items :")

# -------------------------------------------------------
# 1 using remove() method:
# -------------------------------------------------------
fruits = ["apple", "banana", "mango", "kiwi"]
print("Before remove:", fruits)
fruits.remove("kiwi")          # Removes a specific value
print("After remove:", fruits)

# -------------------------------------------------------
# 2 using pop() method:
# -------------------------------------------------------
# -->Removes an element at the given index
# -->If no index is given, it removes the last item
# -->Returns the removed item

fruits = ["apple", "banana", "mango", "Kiwi"]
# without index
print("Before pop:", fruits)
popped_item = fruits.pop()     # Removes last item
print("Popped item:", popped_item)
print("After pop without index:", fruits)

# with index
popped_item = fruits.pop(1)     # Removes  item at index 1
print("Popped item:", popped_item)
print("After pop with index:", fruits)
# -------------------------------------------------------
# 3 using clear() method:
# -------------------------------------------------------
# -->Removes all items
# -->Makes the list empty
# -->Does not delete the list itself.
fruits = ["apple", "banana", "mango", "Kiwi"]
print("Before clear():",fruits)
fruits.clear()
print("After clear():",fruits)
# -------------------------------------------------------------------------------------
# Looping Through a List
# -------------------------------------------------------------------------------------
"""Looping through list items in Python refers to iterating over each element within a list.
   We do so to perform the desired operations on each item. 
   These operations include list modification, conditional operations,
   string manipulation, data analysis, etc.
"""
fruits = ["apple", "banana", "mango", "orange"]

# -------------------------------------------------------
# 1 Simple for loop
# -------------------------------------------------------
print("Simple Loop:")
for fruit in fruits:
    print(fruit)
# -------------------------------------------------------
# 2 Loop with index using range()
# -------------------------------------------------------
print("\nLoop with index:")
for i in range(len(fruits)):
    print(f"Index {i} =", fruits[i])

# -------------------------------------------------------
# 3 Loop using enumerate() → gives index + value
# -------------------------------------------------------
print("\nUsing enumerate():")
for i, fruit in enumerate(fruits):
    print(i
          
          , ":", fruit)

# -------------------------------------------------------
# 4 Loop through list and modify items (uppercase example)
# -------------------------------------------------------
print("\nModify while looping:")
for fruit in fruits:
    print(fruit.upper())

# -------------------------------------------------------
# 5 Loop with condition
# -------------------------------------------------------
print("\nLoop with condition (more than 5 letters):")
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

# -------------------------------------------------------------------------------------
