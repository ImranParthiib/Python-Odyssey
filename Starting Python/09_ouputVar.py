# Output Variables
"""The Python print() function is often used to output variables."""

x = "Python is awesome"
print(x)

# __________In the print() function, you output multiple variables, separated by a comma:____________

x ="Python"
y = "is"
z = "Awesome"
print(x,y,z)

# You can also use the + operator to output multiple variables:
x ="Python "
y = "is "
z = "Awesome "
print(x+y+z)

"""Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome"."""

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

"""x = 5
y = "John"
print(x + y)""" #this is an error

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x =5892
y = "Python"
print(x,y)

a ='Sultan'
b = 'Mehmed'
c = 'Khan'
print(a,b,c)
