#function definitions

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'zero division error'

def calculator(n1, n2 , operator):
    my_dict ={'+': add(n1,n2), '*': multiply(n1,n2),
     '-': subtract(n1, n2), '/': divide(n1, n2)}

    return my_dict[operator]

#user input


n1 = input('enter first number: ').strip()
if n1.isdigit():
    n1 = int(n1)
else:
    n1 = eval(n1)
n2 = input('enter second number: ').strip()
if n2.isdigit():
    n2 = int(n2)
else:
    n2 = eval(n2)

print('\nSelect operation:')
print('(+) for addition')
print('(-) for subtraction')
print('(*) for multiplication')
print('(/) for division')

operator = input('enter respective operator sign from above: ').strip()

#function call

output = calculator(n1, n2, operator)
print('\nCalculation')
print(f'({n1})',operator, f'({n2})',':')
print('\nResult:')
print(output)








