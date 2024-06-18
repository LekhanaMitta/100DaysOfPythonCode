# Day4 - 18th June 2024
# Importing the modules, their variable and function in different ways.

# way - 1
import Module 
courses = ['Art', 'Physics', 'Chemistry', 'Maths']
index = Module.find_index(courses, 'Art')
print("Importing the module using \' import Module \' ")
print(index)

# way - 2
import Module as mod
courses = ['Art', 'Physics', 'Chemistry', 'Maths']
index = mod.find_index(courses, 'Art')
print("Importing the module using \' import Module as mod \' ")
print(index)

# way - 3
from Module import find_index, test
courses = ['Art', 'Physics', 'Chemistry', 'Maths']
index = find_index(courses, 'Art')
print("Importing the module using \' from Module import find_index, test \' ")
print(index)
print(test)

# way - 4
from Module import *
courses = ['Art', 'Physics', 'Chemistry', 'Maths']
index = Module.find_index(courses, 'Art')
print("Importing the module using \' from Module import *\' ")
print(index)

# Some important libraries to import

# 1. sys
import sys
print(sys.path)

# 2. random
import random
print(random.choice(courses))

# 3. Math
import math
print(math.radians(90))
print(math.sin(1.5707963267948966))

# 4. datetime
import datetime
print(datetime.date.today())

# 5. Calender
import calendar
print(calendar.isleap(2002))

# 6. os
import os
print(os.getcwd())
# To print the entire standard library of os module use:
print(os.__file__)

print('--------------------------------------------------------------------------------------')

# Variable scope
# LEGB Rule:
# 1. Local
# 2. Enclosing
# 3. Global
# 4. Built-in

# import builtins
# print(dir(builtins))

x = 'global x'
z = 'global z'
# a = 'global a'
# b = 'global b

def test(h):
    global z
    global a
    # global b
    z = 'local z'
    y = 'local y'
    x = 'local x'
    a = 'local a'
    b = 'local b'
    print(y)
    print(x)        # Checks if there is any local x if it doesn't find then checks for x in global scope and prints x.
    print(z)
    print(h)

# print(y)            # y is not present in the local scope of the main function then checks in the global scope and its still not present.
test('Enclosed variable h')
# output : 
# local y
# local x
# local z
# Enclosed variable h
print(x)
# output : global x
print(a)            # Even if it doesn't contain the variable in it's local scope it printed the value from the global 'a'.
# output : local a
# print(b)            # Not defined.
# print(h)          # Gives nameError where z is not defined.


def my_min():
    print(23)

# Here min is a builtin function. when min function is called it initially checks for any global functions available
# Later it checks for builtin functions. To avoid it change the name of the global function which is similar
# to the name of the builtin function.
m = min([2, 4, 6, 1, 4])
print(m)
# output : 1

my_min()
# output : 23

print('--------------------------------------------------------------------------------------')

# Example :
def outer():
    x = 'outer x'
    y = 'outer y'
    z = 'outer z'
    
    def inner():
        x = 'inner x'
        nonlocal z
        z = 'inner z'

        print(x)
        # output : inner x
        print(y)
        # output : outer y
        print(z)
        # output : outer z
    
    inner()
    print(x)
    # output : outer z
    print(z)
    # output : inner z
    print(y)
    # output : outer y

outer()
print(x)


print('--------------------------------------------------------------------------------------')

