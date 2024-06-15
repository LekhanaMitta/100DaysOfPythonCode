#100DaysOfPythonCode
# 15th June 2024
# Content: 
# 1. Strings - Textual Data
# 2. Integers and Float - Numeric Data

# Variables and DataTypes
print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")

print("-------------------------------------------------------------")

# If the developer wants to change the name of the man to John, and age to 50.
# then he/she has to manually change the name and the age.
print("Manually changing the name :-")
print("There once was a man named John, ")
print("he was 50 years old. ")
print("He really liked the name John, ")
print("but didn't like being 50.")

print("-------------------------------------------------------------")

print("Using Variable to change the name and age :-")

# to reduce the manual work, variable concept is introduced.
# Give name to the variable where we are gonna store the name, age.
character_name = "John"
character_age = "45 "

print("There once was a man named "+ character_name +", ")
print("he was "+character_age+ ", years old. ")

character_name = "Tenzu"
character_age = "25"
print("He really liked the name "+character_name+ ", ")
print("but didn't like being "+character_age+ ".")

print("-------------------------------------------------------------")

# Introducing newline into the print statement
# Whenever a backslash is used in print statement as escape character, it basically tells the python that whatever
# character present next to it needed to be printed literally.
print("Lekhana \nMitta")
# Output : 
# Lekhana
# Mitta

print("Lekhana \" Mitta")
#Output : Syntax error.

# print("Lekhana \ Mitta") for printing backslash as in backslash.
print("Lekhana \' Mitta")
# Output : Lekhana \ Mitta


print("-------------------------------------------------------------")

# Working with strings.
# Printing using a string variable
phrase = "Lekhana Mitta"
print(phrase)

print("-------------------------------------------------------------")

# Function is a block of code that we can run which will perform a specific operation on the data.
# Operation can be modified or fetched data.
# Using a string function.

print("-------------------------------------------------------------")

# Methods we are gonna learn:
# 1. str.lower()
# 2. str.islower()
# 3. str.upper()
# 4. str.isupper()
# 5. len(str)
# 6. str.index(str1/char)
# 7. str.find(str1/char)
# 8. str.count(str1/char)
# 9. str.replace(str1/char, str2/char)
# 10. '+' for concatenation.


print("-------------------------------------------------------------")
# To convert entire string into lower case.
print(phrase.lower())   # o/p: lekhana mitta
print(phrase.islower()) # to know if the phrase is totally lowercase (T or F)

print("-------------------------------------------------------------")

# To convert entire string into upper case.
print(phrase.upper())   # o/p: LEKHANA MITTA
print(phrase.isupper()) # to know if the phrase is totally uppercase (T or F)

print("-------------------------------------------------------------")

# We can also use these functions in combination.
print(phrase.upper().isupper()) 
print(phrase.lower().islower())

print("-------------------------------------------------------------")

# Functions where we pass the string as the parameter
print(len(phrase))

# character to grab from the string.
print(phrase[3]) # indexing starting from 0 to len(string).

# characters to get from the string.
print(phrase[0:10]) # prints all the characters from 0 to 10.

print("-------------------------------------------------------------")

# a function called index is used which specifies the index of a particular string or character is present.
print(phrase.index("k")) # index where first 'k' is present.
print(phrase.index("kha")) # index where the substring 'kha' is present.

print("-------------------------------------------------------------")

# method count(), which counts the frequency of the argument in the method count()
print(phrase.count('Mitta')) # returns 1, since there is only 1 Mitta in the phrase.
print(phrase.count('t')) # returns 2, since there are 2 't' in the phrase.

print("-------------------------------------------------------------")

# method find(), which returns the index of the argument in the method find()
print(phrase.find('Lekh')) # return 0
print(phrase.find('Bhanu')) # returns -1, since the substring Bhanu is not present in the string.

print("-------------------------------------------------------------")

# method replace(), syntax : str.replace(substring to be replaced, substring to be replaced with)
phrase.replace('Lekhana', 'Bhanu') # replacement is not done inplace. Because the replaced string is not set.
print(phrase)
print(phrase.replace('Lekhana', 'Bhanu')) # replacement is done inplace, since the replaced string is returned.
# Alternative approach to make replacement in place.
new_phrase = phrase.replace('Lekhana', 'Bhanu')
print(new_phrase) # new_phrase contains the set phrase.
phrase = phrase.replace('Lekhana', 'Bhanu')
print(phrase)

print("-------------------------------------------------------------")

# Using concatenation method is basically taking a string and
# append another string to the current string using '+'.
print(phrase + " is cool")
phrase1 = " is hot"
print(phrase + phrase1)

print("-------------------------------------------------------------")

# Using f string instead of format
phrase2 = f'{phrase}, {phrase1}'
print(phrase2)

phrase2 = f'{phrase.upper()}, {phrase1}'
print(phrase2)

print("-------------------------------------------------------------")

# dir function is used to get all the attributes and methods that we have access to the argument passed into 
# the function.

print(dir(phrase))
# to know the attributes and their details we can use help()
print(help(str)) # gives information about the string datatype.

print("-------------------------------------------------------------")

# On June 14th
print('------------------------------------------------------------------------------')
# function type() is used to know the datatype of the argument.
num = 3
print(type(num))

num = 3.14
print(type(num))

print('------------------------------------------------------------------------------')
# Arithematic Operators:
# 1. Addition : num1 + num2
# 2. Substraction : num1 - num2
# 3. Multiplication: num1 * num2
# 4. Division : num1/num2
# 5. Floor Division : num1//num2
# 6. Exponent : num1 ** num2
# 7. Modulus : num1 % num2

num1 = 5
num2 = 3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1/num2) # python3 returns float type, while python2 returns int type.
print(num1//num2)
print(num1 % num2)
print(num1 ** num2)

print('------------------------------------------------------------------------------')

# Increment, Decrement operator.
num = 3
num += 4
print(num)
num -= 4
print(num)
num *= 4
print(num)
num /= 4
print(num)

print('------------------------------------------------------------------------------')

# abs() method. To get the absolute value of the argument.
print(abs(-1))
print(abs(0))
print(abs(3))

print('------------------------------------------------------------------------------')

# round() method. To get the rounded off value
# round(num, length). To get the nearest decimal rounded to length decimal points.
print(round(1.2345))
print(round(2.745))
print(round(3.5))
print(round(2.345,1))
print(round(1.3425, 3))

print('------------------------------------------------------------------------------')

# Comparisons:
# 1. Equal num1 == num2
# 2. Not equal num1 != num2
# 3. Greater than num1 > num2
# 4. Less than num1 < num2
# 5. Greater than or equal to num1 >= num2
# 6. Less than or equal to num1 <=  num2

num1 = 5
num2 = 6

print(num1 == num2)
print(num1 != num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 > num2)
print(num1 < num2)

print('------------------------------------------------------------------------------')

# Typecasting of string to int
num1 = '100'
num2 = '200'
print(num1 + num2) # Concatenates num1 with num2
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)

print('------------------------------------------------------------------------------')

