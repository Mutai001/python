# Data strustures are used to store and organize data in a computer so that it can be used efficiently.
# Python provides several built-in data structures for handing and managing data efficiently.

#Data structures can be classified into two categories:
# 1. Primitive Data Structures  - These are the basic data structures that directly operate upon the machine instructions.
    #They are basic building blocks for data manipulation and contain the simplest values.
    #Examples: Integers, Floats, Strings, Booleans
    
# a. Integers
x = 5
print(x)
print(type(x))

# b. Floats
y = 5.5
print(y)
print(type(y))

# c. Strings
name = "Alice"
print(name)
print(type(name))

# d. Booleans
z = True
print(z)
print(type(z))


# 2. Non-Primitive Data Structures - These are more advanced data structures that are used to store multiple elements.
    #They are more complex data structures and are derived from primitive data structures.
    #They are used to store a collection of elements.
    #Examples: Arrays, Lists, Stacks, Queues, Trees, Graphs, etc.

    
# a. Arrays - Arrays are used to store multiple elements of the same data type.
    #Example: Array of integers
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
print(a)
print(type(a))

# b. Lists - Lists are used to store multiple elements of different data types.
    #Example: List of integers and strings
fruits = ["apple", "banana", "cherry"]
print(fruits)   
print(type(fruits))

# c. Tuples - Tuples are used to store multiple elements of different data types.
    #Example: Tuple of integers and strings
point = (4, 5)
print(point)
print(type(point))

# 



# Data Structure	Example	Description
# list	        fruits = ["apple", "banana"]	        Ordered, mutable collection
# tuple	        point = (4, 5)	                    Ordered, immutable collection
# dict	        person = {"name": "Alice", "age": 25}	Key-value pair storage