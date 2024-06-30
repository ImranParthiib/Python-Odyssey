def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def mod(num1,num2):
    return num1 % num2

print("Select operation:'+','-','*','/'or'%'")
inp = input("Enter operator:")
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = 0
if inp == '+':
    result = add(num1,num2)
elif inp == '-':
    result = sub(num1,num2)
elif inp == '*':
    result = mul(num1,num2)
elif inp == '/':
    result = div(num1,num2)
elif inp == '%':
    result = mod(num1,num2)
else:
    print("Invalid operator")
print(num1, inp, num2, '=', result)


