print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

# In Python, the built-in print() function is used to output text or other data to the console. The basic syntax is as follows:
print("Hello, world!")


# You can also print multiple items by separating them with commas:
print("Hello,", "world!")


# You can use the + operator to concatenate strings:
print("Hello, " + "world!")


# You can also use f-strings (formatted string literals) in Python 3.6+ to include the values of variables in a string.
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


# You can also use .format() method with {} as placeholder for variables.
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))


# You can also use the % operator to format strings.
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))


# You can also redirect the output of the print() function to a file by passing the file argument:
with open('output.txt', 'w') as f:
    print("Hello, world!", file=f)

# These are some basic examples of using the print() function in Python,
# but there are many other ways to customize and control the output of your program.

# By default, the print() function adds a newline character at the end of the output.
# If you don't want to add a newline, you can pass the end argument with an empty string: print("Hello, world!", end='').

# You can also change the separator between multiple items passed to the print() function.
# By default, it is a space character, but you can change it to any other string by passing the sep argument:
# print("Hello,", "world!", sep=', ').

# You can also use the print() function to output binary data by passing the flush parameter as True.

# You can use print() function to print output in different color by using colorama
# library which can be installed by pip install colorama