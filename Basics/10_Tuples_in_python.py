# -------------------------------------------------------------------------------------
# Tuples in Python
# -------------------------------------------------------------------------------------
"""
A tuple is an ordered, immutable collection of elements.
It is similar to a list, but once created, the values cannot be changed.
Key Features:
- Ordered
- Immutable
- Allow duplicate values
- Can store mixed data types
"""
# -------------------------------------------------------------------------------------
# ------------------- Creating Tuples -------------------
# -------------------------------------------------------------------------------------
# Empty tuple
tuple1 = ()
print("Empty tuple:", tuple1)

# Tuple with elements
num =(10,20,30,40,50,60)
print("Tuple of number:",num)
tuple2 = ("a", "b", "c", "d")
print("Tuple of character:",tuple2)

# Mixed data type
mixtuple = ("Harshad",21,"Mhatre",72.5,True,12.89)
print("Mixed tuple:",mixtuple)

# Tuple without parentheses (Tuple packing)
fruits = "Apple", "Banana", "Cherry"
print("Tuple without parentheses:", fruits)
# -------------------------------------------------------------------------------------
# ------------------- Tuple with One Element -------------------
# -------------------------------------------------------------------------------------
#To write a tuple containing a single value you have to include a comma,even though there is only one value
tup1 = (78,) #comma necessary

# ------------------- Accessing Elements from Tuple-------------------
"""To access values in tuple, use the square brackets for slicing along with the index 
   or indices to obtain value available at that index"""
print("\nAccessing Elements from Tuple:")
car_brands=("BMW","Tata","Honda","Mahindra","Mercedes")
print("First element:", car_brands[0])
print("Last element:", car_brands[-1])
# -------------------------------------------------------------------------------------
# ------------------- Slicing Tuple-------------------
# -------------------------------------------------------------------------------------
# The slice operator in Python is used to fetch one or more items from the tuple
# Syntax [start:stop] 
print("\nTuple Slicing:")
tup3=(10,23,34,30,45,60,78,80)
print("Slice [1:]:", tup3[1:])
print("Slice [0:2]:", tup3[0:2])
print("Reverse tuple:", tup3[::-1])
print("Slice from index 2 to 5",tup3[2:6])
print("Slice first four elements",tup3[:4])
print("Every Second element",tup3[::2])

# -------------------------------------------------------------------------------------
# ------------------- Updating Tuple-------------------
# -------------------------------------------------------------------------------------
# Tuples are immutable which means you cannot update or change the values of tuple elements
# You are able to take portions of existing tuples to create new tuples
print("\nUpdating Tuple:")
tup1 =(12,34.56)
tup2 =('abc','xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

#  create a new tuple by combining both tuples
tup3 = tup1 + tup2 #using + operator
print (tup3)
# -------------------------------------------------------
# using slice operator
# -------------------------------------------------------
t1=(10,20,30,40,50,60,70,80,90)
words=("one","two","three","four","five")

t2=t1[0:3] #slicing desired part from tuple
t3=t1[5:7] #slicing desired part from tuple
print(t1)
print(words)
print("Sliced t2:",t2)
print("Sliced t3:",t3)
new_tuple=t2+words+t3 #combining parts in a new tuple
print("New combined tuple:",new_tuple)

# -------------------------------------------------------
# Updating Tuples using List Comprehension
# -------------------------------------------------------
tup1=(10,20,30,40)
# Converting the tuple to a list
list_t1 = list(tup1)
# Using list comprehension 
list_t1[2] = 33
list_t1[0] = 50

# Converting the updated list back to a tuple
new_tuple = tuple(list_t1)
# Printing the updated tuple
print("Original Tuple:", tup1)
print("Updated Tuple:", new_tuple)
# -------------------------------------------------------
# # Updating Tuple using append() method after converting to list
# -------------------------------------------------------
tup2=(23,45,56,67,78,70,30)
list_t2 = list(tup2) # Converting the tuple to a list
element=[100,110,120]
for i in element:
    list_t2.append(i)

new_tuple1 = tuple(list_t2)  # Converting the updated list back to a tuple  
print("Original Tuple:", tup2)
print("Updated Tuple:", new_tuple1)
# -------------------------------------------------------------------------------------
# ------------------- Iterating a Tuple -------------------
# -------------------------------------------------------------------------------------
tup4 = (25,-12,10,21,-10,100)
print("\nLooping using for loop")
for num in tup4:
   print (num, end = ' ')
# -------------------------------------------------------------------------------------
# ------------------- Tuple methods-------------------
# -------------------------------------------------------------------------------------
# count() ->	Returns how many times a value appears in a tuple
# index() ->	Returns the index of the first occurrence of a value
tup5 = (25, 12, 10, -21, 10, 100)
print ("\nTup5:", tup5)
a= tup1.index(10)
print ("First index of 10:",i)

tup6 = (10, 20, 45, 10, 30, 10, 55)
print ("Tup6:", tup6)
b = tup1.count(10)
print ("count of 10:",b)
# -------------------------------------------------------------------------------------