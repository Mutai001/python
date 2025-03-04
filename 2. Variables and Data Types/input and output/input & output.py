#Python allows interaction with users through input and output functions.

# 🔹 Output: print()

# The print() function is used to display text, numbers, or other data on the screen.
# You can pass multiple arguments to print(), separated by commas.
# print() automatically adds a newline character at the end of the output.
# You can use the end parameter to specify a different character to append at the end.
# You can use the sep parameter to specify a different character to separate the arguments.
#✅ Example:

print("Hello, World!")
name = "Cyrus"
print("My name is", name)
print("Hello", "World", sep=", ", end="!\n") 




# 🔹 Input: input()

# The input() function is used to read input from the user.
# input() returns the user's input as a string.
# You can use the int() function to convert the input to an integer.
# You can use the float() function to convert the input to a floating-point number.
#✅ Example:

name = input("Enter your name: ")
print("Hello,", name)
