"""**************___Python Numbers____***************"""

# There are three numeric types in Python:

# int
# float
# complex

# Variables of numeric types are created when you assign a value to them:

# Example 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# To verify the type of any object in Python, use the type() function:

"""Example"""

print(type(x))
print(type(y))
print(type(z))

"""Int"""
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

"""Example"""
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

"""Float"""
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Example

x = 7.67
y = 89.0
z = -87.6876

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.


"""  Complex"""

# Complex numbers are written with a "j" as the imaginary part:
# Example

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

"""Type Conversion"""
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 30
y = 33.90
z = 33j

a = float(x)
b = complex(y)
c = int(z.imag)

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

"""Random Number"""
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# Example  
# Import the random module, and display a random number between 1 and 9:
 
import random 

print(random.randrange(1,99))



