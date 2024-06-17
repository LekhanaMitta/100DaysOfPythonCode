# On June 17th 2024
# If, else and elif statements:
print('------------------------------------------------------------------------------')

# If statement
# Executes the statement when the condition is true.
# This prints "conditional was true."
if True:
    print('Conditional was true')

if False:
    print('Conditional was true')

language = 'Python'

# This print statement gets printed.
if language == 'Python':
    print('Condition was True.')

if language == 'Java':
    print('Condition was True.')

print('------------------------------------------------------------------------------')

# If-else statement.

if language == 'Python':
    print('Language is Python.')
else:
    print('Language is not Python.')

print('------------------------------------------------------------------------------')

#Elif statement.

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java.')
else:
    print('It is a different language.')

print('------------------------------------------------------------------------------')

# Using Boolean 
# and
# or
# not

user = 'admin'
logged_in = False

# (Prints the else statement)
if user == 'admin' and logged_in:
    print('Admin Page')
else:
    print('bad Credentials')

# Prints if statement
if user == 'admin' or logged_in:
    print('Admin Page')
else:
    print('bad Credentials')

# Prints if statement
if user == 'admin' and not logged_in:
    print('Admin Page')
else:
    print('bad Credentials')

print('------------------------------------------------------------------------------')

# Comparing two lists with their id's.
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b)                       # It is false, since the id's of a and b are not same.

b = a
print(id(a))
print(id(b))
print(a is b)                       # It is true, since the id of a is assigned to b as well.

print('------------------------------------------------------------------------------')

# Python conditions that evaluate to false values:
# 1. False
# 2. None
# 3. Zero of any numeric type
# 4. Any empty sequence. Ex : (), '', []
# 5. Any empty mapping. Ex: {}

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0.0 or 0
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = '' or [] or ()
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

print('------------------------------------------------------------------------------')

# Loops and Iterations

print('--------------------------------------------------------------------------')

# For loop
nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    print(num)

print('--------------------------------------------------------------------------')

# Break statement
for num in nums:
    if num == 3:
        break
    print(num)
# 3 doesn't get printed since, the for loop breaks when num = 3.

print('--------------------------------------------------------------------------')

# Continue Statement - will ignore the value when condition is true and escapes the remaining 
# statements.
for num in nums:
    if num == 3 or num == 5:
        continue
    print(num)

print('--------------------------------------------------------------------------')

# Loop within a loop.
# Prints every combinational pair of (num, letter)
for num in nums:
    for letter in 'abc':
        print(num, letter)

print('--------------------------------------------------------------------------')

# range(a, b) - considering from a and upto b(not including).
for i in range(0, 12):
    print(i)

print('--------------------------------------------------------------------------')

# While loop will keep going until a certain condition is met or interrupted through keyboard.
x = 0
while x<10:
    print(x)
    x += 1

print('--------------------------------------------------------------------------')

# Break statement in while loop
x = 0
while x<10:
    if x == 5:
        break
    print(x)
    x += 1

print('----------------------------------while----------------------------------------')

# Continue statement in while loop
x = 0
while x<10:
    x = x + 1
    if (x % 2) == 1:
        continue
    print(x)


    

print('--------------------------------------------------------------------------')

def print_hello():
    return "Hello from Function!!"

print('Hello from print statement!!')
print('Hello from print statement!!')
print('Hello from print statement!!')
print('Hello from print statement!!')
print('Hello from print statement!!')

# The below 2 lines of code prints Hello as many times as the above code prints
for i in range(0,5):
    print_hello()

print('------------------------------------------------------------------------')

# Function which returns the values.

def print_hello():
    return 'Hello from the return Function!'

# How to print the returned value.
print(print_hello())

# Since the executed function is string, we can apply the methods on the returned value.
# 1. Upper()
print(print_hello().upper())
# 2. lower()
print(print_hello().lower())
# 3. len()
print(len(print_hello()))
# 4. format()
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func("Hello"))

def hello_func(greeting, name):
    return '{}, {}.'.format(greeting, name)

print(hello_func('Hello', 'Lekhana'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Art', 'Maths', name = 'Lekhana', grade = 12)
# output :
# ('Art', 'Maths')
# {'name': 'Lekhana', 'grade': 12}

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Art', 'science']
info = {'name' : 'Lekhana', 'age' : 22}
student_info(courses, info)
# output :
# (['Art', 'science'], {'name': 'Lekhana', 'age': 22})
# {}
# * in args unpacks the list, and ** in kwargs unpack the dictionary

student_info(*courses, **info)
# output :
# ('Art', 'science')
# {'name': 'Lekhana', 'age': 22}

print('------------------------------------------------------------------------')

# Exercise : 
# Number of days in a year of a particular month.

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(x):
    return x % 4 == 0 and (x % 100 != 0 or x % 400 == 0)

def days_in_month(month):
    if x <= 0 or x > 12:
        return 'Invalid Month'
    if month == 2 and leap_year(month):
        return 29
    return month_days[month]

print(days_in_month(8))

print('------------------------------------------------------------------------')