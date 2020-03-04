# Variables

# Variable Decln and Intian
f = 0
print(f)

# Redeclaring var
f = 'abc'
print(f)

# Variables of different types can not be combined
print('Mixing a string with number ' + str(123))
# Python is a strongly typed language. And does not allow mixing types of vars. Unlike JS

# Global vs local variables in functions

def someFunction():
    f = "def"
    print(f)

someFunction()
print(f)

g = "local"

def someFunction2():
    global g  # will overwrite the global variable if the fn is executedß
    g = "global"
    print(g)

someFunction2()
print(g)

del g # deletes a previously created variable
print(g) # g is not defined