"""***********Many Values to Multiple Variables***********"""
# Python allows you to assign values to multiple variables in one line:
x, y, z = "Sultan ", "Mehmed ", "Khan "
print(x)
print(y)
print(z)
print(x+y+z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

"""One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:"""

# Example 
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
"""If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking."""

name =["Sultan ","Mehmed ","Khan"]
firstName,middleName,lastName = name

print(name)
print(firstName)
print(middleName)
print(lastName)
print(firstName+middleName+lastName)