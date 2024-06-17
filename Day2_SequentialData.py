# On 16th June 2024.
print("-------------------------------------------------------------")
# List 
courses = ['Maths', 'Physics', 'Chemistry', 'Sanskrit']
print(len(courses))             # number of elements present in the list
# output : 4
print(courses)                  # to print the elements of the list
# output : ['Maths', 'Physics', 'Chemistry', 'Sanskrit']
print(courses[0])               # To print the element that is present at the index.
# output : Maths
print(courses[-1])              # To print the last element of the list.
# output :Sanskrit

print("-------------------------------------------------------------")

# List Comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# If we want n for every n in nums
num_list = []
for n in nums:
    num_list.append(n)
print(num_list)

# List Comprehension
num_list = [n for n in nums]
print(num_list)

# If we want n*n for each 'n' in nums
num_list = []
for n in nums:
    num_list.append(n*n)
print(num_list)

# Using a map + lambda
num_list = list(map(lambda n: n*n, nums))
print(num_list)

# If we want n for each n in nums if n is even.
num_list = []
for n in nums:
    if n%2 == 0:
        num_list.append(n)
print(num_list)

num_list = [n for n in nums if n%2 == 0]
print(num_list)

# Using filter + lambda function
num_list = list(filter(lambda n: n%2==0, nums))
print(num_list)

print("-------------------------------------------------------------")

# Slicing of the list.
print(courses[0:2])             # To print the elements that are in between the indices 0(including) to 2(excluding)
# output : ['Maths', 'Physics']
print(courses[:3])              # To print elements from the start to index(excluding)
# output : ['Maths', 'Physics', 'Chemistry']
print(courses[2:])              # To print elements from index(including) to end of list.
# output : ['Chemistry', 'Sanskrit']
# print(courses[5])             # any index given that is greater than the length of the list gives error
# Gives IndexError : list index out of range.

my_list = [2, 4, 6, 3, 5, 8, 9, 11, 10]
# index -  0  1  2  3  4  5  6   7  8  
# index - -9 -8 -7 -6 -5 -4 -3  -2 -1

# To print a range of elements from the list.
#list[start : end : step] 
# end - not inclusive, step - how many indices are skipped.
print(my_list[0: 9: 2])         # output : [2, 6, 5, 9, 10]
print(my_list[2:-4: 2])         # output : [6, 5]
print(my_list[5:-10:1])         # output : []
print(my_list[5:-10:-1])        # output : [8, 5, 3, 6, 4, 2]
# To print the list in reverse order.
print(my_list[: :-1])

print("-------------------------------------------------------------")

# Append() method, used to add the element into the list.
courses.append('Computer Science')
print(courses)
# output : ['Maths', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science']
print(courses[len(courses)-1])
# output : Computer Science

# Append a list into another list.
courses.append(['Telugu', 'English'])
print(courses)
# output : ['Maths', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English']]
print(courses[len(courses)-1])
# output : 
# output : ['Telugu', 'English']

print("-------------------------------------------------------------")

# Insert() method, to insert the element into the list at a specific index.
courses.insert(0, 'Arts')
print(courses)
# output : ['Arts', 'Maths', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English']]
print(courses[0])
# output : Arts

# Inserting a list into another list.
course1 = ['Biology', 'History']
courses.insert(0, course1)
print(courses)
# output : [['Biology', 'History'],'Arts', 'Maths', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English']]
print(courses[0])
# output : ['Biology', 'History']
print("-------------------------------------------------------------")

# extend() method, is used to extend the elements of the course1 into courses
# as in elements but not as list.
course1 = ['Geology', 'Zoology', 'Botany']
courses.extend(course1)
print(courses)
# output : [['Biology', 'History'],'Arts', 'Maths', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English'], 'Geology', 'Zoology', 'Botany']


print("-------------------------------------------------------------")

# remove() method, is used to delete an element with element itself as argument.
courses.remove('Maths')
print(courses)
# output : [['Biology', 'History'],'Arts', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English'], 'Geology', 'Zoology', 'Botany']


print("-------------------------------------------------------------")

# pop() method, is used to delete an element that is present at the end of the list.
courses.pop()
print(courses)
# output : [['Biology', 'History'],'Arts', 'Physics', 'Chemistry', 'Sanskrit', 'Computer Science', ['Telugu', 'English'], 'Geology', 'Zoology']


print("-------------------------------------------------------------")

# reverse() method, reversing the list.
print("reverse()")
courses.reverse()
print(courses)
# output : ['Zoology', 'Geology', ['Telugu', 'English'], 'Computer Science', 'Sanskrit', 'Chemistry', 'Physics', 'Arts', ['Biology', 'History']]

print("-------------------------------------------------------------")

# sort() method, sorting the list. This will not work if the list contains other lists
courses = ['Zoology', 'Geology', 'Art', 'Computer Science', 'Physics']
courses.sort()
print(courses)
# output : ['Art', 'Computer Science', 'Geology', 'Physics', 'Zoology']

courses.sort(reverse=True)      # To sort the elements in the list in decreasing order.
print(courses)
# output : ['Zoology', 'Physics', 'Geology', 'Computer Science', 'Art']

# sorted(list) is used to sort the elements of the list and returns the sorted list.
courses = ['Zoology', 'Geology', 'Art', 'Computer Science', 'Physics']
sorted(courses)
print(courses)                  # This will not sort the list in increasing order.
# output : ['Zoology', 'Geology', 'Art', 'Computer Science', 'Physics']
print(sorted(courses))          # This will print the sorted list since sorted is return function.
# output : ['Art', 'Computer Science', 'Geology', 'Physics', 'Zoology']

print("-------------------------------------------------------------")

# min(), max() and sum() methods
nums = [1, 6, 8, 13, 14, 34]
print(min(nums))    # output : 1
print(max(nums))    # output : 34
print(sum(nums))    # output : 76

print("-------------------------------------------------------------")

# Finding the elements
print(courses.index('Geology'))             # output : 1
# print(courses.index('Math'))              # gives valueError since
# ValueError - since there is no value as that of the argument passed.
print('Art' in courses)                     # output : True

# Syntax for "for" loop which prints the elements of list one on one
for item in courses:
    print(item)
# output : 
# Zoology
# Geology
# Art
# Computer Science
# Physics

# Printing both the index and element of the lists with default index as 0:
for idx, item in enumerate(courses):
    print(idx, item)
# output : 
# 0 Zoology
# 1 Geology
# 2 Art
# 3 Computer Science
# 4 Physics

# Printing both the index and element of the lists where indexing starts from 1:
for idx, item in enumerate(courses, start = 1):
    print(idx, item)

print("-------------------------------------------------------------")

# Splitting Values.
# join() method, To print ',' after every list element:
course_Str = ','.join(courses)
print(course_Str)
# output : Zoology,Geology,Art,Computer Science,Physics

# To print elements that are seperated by a character.
# split() method.
course_Str = ' - '.join(courses)
new_list = course_Str.split(' - ')
print(course_Str)
# output : Zoology - Geology - Art - Computer Science - Physics
print(new_list)
# output : ['Zoology', 'Geology', 'Art', 'Computer Science', 'Physics']

print("-------------------------------------------------------------")

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
# output : ['History', 'Math', 'Physics', 'CompSci']
print(list_2)
# output : ['History', 'Math', 'Physics', 'CompSci']

list_1[0] = 'Biology'
print(list_1)
# output : ['Biology', 'Math', 'Physics', 'CompSci']
print(list_2)
# output : ['Biology', 'Math', 'Physics', 'CompSci']

print("-----------------------Tuples--------------------------------------")

# Immutable/ Tuples
tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
tuple_2 = tuple_1
print(tuple_1)
# output : ('History', 'Math', 'Physics', 'CompSci')
print(tuple_2)
# output : ('History', 'Math', 'Physics', 'CompSci')

# This will throw a TypeError
# tuple_1[0] = 'Art'
# print(tuple_1)
# print(tuple_2)

tup = (9, 1, 8, 4, 5, 7, 2, 3, 6)
# tup.sort() throws attributeError

s_tup = sorted(tup)
print(s_tup)
# output : [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("-------------------------------------------------------------")

# Sets
course = {'History', 'Math', 'Physics', 'Compsci'}
print(course)
# output : {'Math', 'History', 'Physics', 'Compsci'}

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Physics', 'Art', 'Design'}

print('Math' in cs_courses)
# output : True
print('Art' in art_courses)
# output : True

print("-------------------------------------------------------------")

# Intersection method(), set1.intersection(set2)
print(cs_courses.intersection(art_courses))
# output : {'History', 'Physics'}

# Difference method(), set1.difference(set2)
print(cs_courses.difference(art_courses))
# output : {'Math', 'CompSci'}

# Union method(), set1.union(set2)
print(cs_courses.union(art_courses))
# output : {'Art', 'History', 'CompSci', 'Design', 'Math', 'Physics'}

print("-------------------------------------------------------------")

# Empty sets, tuples and lists.
empty_list = []
empty_list = list()
print(empty_list)
# output : []

empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)
# output : ()

# empty_set = {}  # It's wrong, which is used for dictionaries.
empty_set = set()
print(empty_set)
# output : {}
nums = [1, 2, 1, 2, 3, 1, 1, 5, 3, 6, 7, 8, 4, 4, 9]
my_set = set()
for s in nums:
  my_set.add(s)
print(my_set)
# output : {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set = {n for n in nums}
print(my_set)
# output : {1, 2, 3, 4, 5, 6, 7, 8, 9}


# print("-------------------------------------------------------------")

# Working with Key Value Pair
print('--------------------------------------------------------------------------------------')

student = {'First Name' : 'Lekhana', 'Last Name' : 'Mitta', 'Age' : 22, 'Courses' : ['Math', 'Physics', 'Chemistry']}
print(student['Courses'])
# output : ['Math', 'Physics', 'Chemistry']
print(student['Age'])
# output : 22

print('--------------------------------------------------------------------------------------')

# Methods in Dictionary
# get() method
print(student.get('First Name'))
# output : Lekhana
print(student.get('phone'))                     # prints none
print(student.get('phone', 'Not Found'))        # prints Not Found
student['phone'] = '234567'
print(student.get('phone'))
# output : 234567

print('--------------------------------------------------------------------------------------')

# Updating the values of the dictionary
student['First Name'] = 'Bhanu'
print(student)
# output : {'First Name': 'Bhanu', 'Last Name': 'Mitta', 'Age': 22, 'Courses': ['Math', 'Physics', 'Chemistry'], 'phone': '234567'}
student.update({'Last Name' : 'Reddy', 'Age' : 22})
print(student)
# output : {'First Name': 'Bhanu', 'Last Name': 'Reddy', 'Age': 22, 'Courses': ['Math', 'Physics', 'Chemistry'], 'phone': '234567'}

print('--------------------------------------------------------------------------------------')

# Deleting the values of the dictionary
del student['phone']
print(student)
# output : {'First Name': 'Bhanu', 'Last Name': 'Reddy', 'Age': 22, 'Courses': ['Math', 'Physics', 'Chemistry']}
age = student.pop('Age')
# output : {'First Name': 'Bhanu', 'Last Name': 'Reddy','Courses': ['Math', 'Physics', 'Chemistry']}
print(student)

print('--------------------------------------------------------------------------------------')

# Keys(), values() and items()
print(student.keys())                   # prints keys of the dictionary
# output : dict_keys(['First Name', 'Last Name', 'Courses'])
for key in student:
    print(key)
# output :
# First Name
# Last Name
# Courses

print(student.values())                 # prints values of the dictionary
# output : dict_values(['Bhanu', 'Reddy', ['Math', 'Physics', 'Chemistry']])
for key, value in student.items():
    print(key, value)
# output : 
# First Name Bhanu
# Last Name Reddy
# Courses ['Math', 'Physics', 'Chemistry']

print(student.items())                  # prints items of the dictionary as they are.
# output : dict_items([('First Name', 'Bhanu'), ('Last Name', 'Reddy'), ('Courses', ['Math', 'Physics', 'Chemistry'])])

print('--------------------------------------------------------------------------------------')

# Dictionary Comprehension
names = ['Albert Einstein', 'Marie Curie', 'Ramanujan', 'Swaminathan']
courses = [' Physics', 'Chemistry', 'Mathematics', 'Botany']
print(list(zip(names, courses)))
# output : [('Albert Einstein', ' Physics'), ('Marie Curie', 'Chemistry'), ('Ramanujan', 'Mathematics'), ('Swaminathan', 'Botany')]

my_dict = {}
for name, course in list(zip(names, courses)):
    my_dict[name] = course
print(my_dict)
# output : {'Albert Einstein': ' Physics', 'Marie Curie': 'Chemistry', 'Ramanujan': 'Mathematics', 'Swaminathan': 'Botany'}

my_dict = {name: course for name, course in list(zip(names, courses)) }
print(my_dict)
# output : {'Albert Einstein': ' Physics', 'Marie Curie': 'Chemistry', 'Ramanujan': 'Mathematics', 'Swaminathan': 'Botany'}

# sorting a dictionary.
# Key values are sorted.
s_di = sorted(my_dict)
print(s_di)
# output : ['Albert Einstein', 'Marie Curie', 'Ramanujan', 'Swaminathan']


print('--------------------------------------------------------------------------------------')

# String Formatting.
person = {'Name':'Lekhana', 'age':22, 'Education' : 'Bachelors'}
tag = "h1"
text = "This is FYI."
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)
# output : <h1>This is FYI.</h1>

sentence = 'My name is {0}, I am {1} years old and I completed my {2}'.format(person['Name'], person['age'], person['Education'])
print(sentence)
# output : My name is Lekhana, I am 22 years old and I completed my Bachelors

sentence = 'My name is {0[Name]}, I am {1[age]} years old and I completed my {2[Education]}'.format(person, person, person)
print(sentence)
# output : My name is Lekhana, I am 22 years old and I completed my Bachelors

person = ['Lekhana', 22, 'Bachelors']
sentence = 'My name is {0[0]}, I am {0[1]} years old and I completed my {0[2]}'.format(person)
print(sentence)
# output : My name is Lekhana, I am 22 years old and I completed my Bachelors

sentence = 'My name is {name}, I am {age} years old and I completed my {education}'.format(name = 'Lekhana', age = 22, education = 'Btech')
print(sentence)
# output : My name is Lekhana, I am 22 years old and I completed my Btech

