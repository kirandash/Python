# Functions

# Basic Fn
def func1():
    print('A basic function')

func1() # inner prints 
print(func1()) # inner prints ---> return nothing for outer print ---> None
print(func1) # prints the fn object which can be passed around to other python code like we did ehre

# Fn with args
def func2(arg1, arg2):
    print(arg1, " ", arg2)

func2(10, 20)

# Fn that returns a value
def square(x):
    return x * x

print(square(3))

# Fn with default val for an arg
def power(num, x=1): # default val for x
    result = 1
    for i in range(x): # loop
        result = result * num
    return result

print(power(2)) # x = 1
print(power(2, 3)) # x = 3
print(power(x=3, num = 2)) # same as above, python supports name and value declaration. Thus order can be ignored

# Fn with variable no of args
def multi_add(*args): # multiple args can be sent as *args
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(2,3,5,15))

# Note: Variable args can be combined with a set of formal args but var args in that case should always come at end
def multi_add_offset(num1, num2, *extranums):
    result = num1 - num2
    for x in extranums:
        result = result + x
    return result

print(multi_add_offset(30, 5, 4, 1))