"""The global Keyword"""
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

def my_func():
    global x
    x ="Learning is Fun"
    print(x)

my_func()    


print(x)


"""Also, use the global keyword if you want to change a global variable inside a function."""

# Example 
"""To change the value of a global variable inside a function, refer to the variable by using the global keyword:"""

y ="Life is Amazing & challenging"

def my_Life():
    global y 
    y = "Life is a journey of uncertainty"
    print(y)

my_Life()

print(y)

