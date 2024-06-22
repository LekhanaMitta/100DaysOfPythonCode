# 20th June 2024
# Important modules like DataTime, OS, random, CSV

# os module allows us to interact with the underlying operating systems in several different ways:
# 1. Navigate the file system.
# 2. Get file information.
# 3. Move files around.

# Builtin module
import os

# To know the attributes and variables that can be accessed from the module can be printed using:
# print(dir(os))

# To get the current directiory we are in:
print(os.getcwd())

print('-------------------------------------------------------------------------------------------------------------')

# If we to navigate to different location use: chdir() -  change directory.
os.chdir('C:/Users/lekha/OneDrive/Documents')
print(os.getcwd())

print('-------------------------------------------------------------------------------------------------------------')

# To get the files and folders present in a particular/current directory:
# print(os.listdir())

# To create a folder or directory in the current directory use:
os.chdir('C:/Users/lekha/OneDrive/Documents/100DaysOfPythonCode')
print(os.getcwd())
print(os.listdir())
os.mkdir('OS_module.txt')
print(os.listdir())

print('-------------------------------------------------------------------------------------------------------------')

# makedirs() and makedir() are almost same but makedir() won't be able to create directory that is deeper.
# while makedirs() is used to create a directory that can go deeper.
# os.dir('osModule/os_module.txt')      # This gives an error, since makedir() can't go deeper.
os.makedirs('os_module2.txt')            # This is as normal as makedir('os_module.txt)
os.makedirs('osModule/os_module1.txt')   # This creates a os_module.txt sub directory in osModule directory.
print(os.listdir())

print('-------------------------------------------------------------------------------------------------------------')

# deleting the folders or directories:
# rmdir() and removedirs() are almost similar but the difference is that rmdir() can't delete the folders 
# while removedirs() can be able to delete the folders.
os.rmdir('OS_module.txt')               # Deletes the files   
os.removedirs('os_module2.txt')         # deletes the file.
os.removedirs('osModule/os_module1.txt')# deletes the directory.
print(os.listdir())

print('-------------------------------------------------------------------------------------------------------------')

# Renaming and file or a folder: rename()
os.rename('rename_test.txt', 'test.txt')
print(os.listdir())
os.rename('test.txt', 'rename_test.txt')

print('-------------------------------------------------------------------------------------------------------------')
# If we want to print out the information about a file:
print(os.stat('rename_test.txt'))
print(os.stat('rename_test.txt').st_atime)

# To get the time stamps into human readable format, so we have to import dateTime 
from datetime import datetime
mod_time = os.stat('rename_test.txt').st_atime
print(datetime.fromtimestamp(mod_time))

print('-------------------------------------------------------------------------------------------------------------')

# If we to see the entire directory tree and files within the current directory.
os.chdir('C:/Users/lekha/OneDrive/Documents')

# This top to down process:
for dirpath, dirnames, filenames in os.walk('C:/Users/lekha/OneDrive/Documents/100DaysOfPythonCode'):
    print('Current Path is : ', dirpath)
    # print('Current Directory is : ', dirnames)
    # print('Files in the directory : ', filenames)

print('-------------------------------------------------------------------------------------------------------------')

# To get the environment directory:
# print(os.environ.get('HOME'))
# To create a file in our home directory:
# filepath = os.environ.get('HOME') + 'test2.txt'
# print(filepath)
# filepath = os.path.join(os.environ.get('HOME'), 'test2.txt')
# print(filepath)

print(os.path.basename('/bhanu/test.txt'))          # Prints the base name
print(os.path.dirname('/bhanu/test.txt'))           # prints the name of the directory.
print(os.path.split('/bhanu/test.txt'))             # prints both the file and directory name.
print(os.path.exists('/bhanu/test.txt'))            # check whether the given file path exists or not.

# If a file or directory actually exists on the path to check whether it is a file or directory we can use:
print(os.path.isdir('C:/Users/lekha/OneDrive/Documents/100DaysOfPythonCode'))
print(os.path.isfile('C:/Users/lekha/OneDrive/Documents/100DaysOfPythonCode/image.jpg'))

# To get the split of the file route with the extension we can use:
print(os.path.splitext('/bhanu/test.txt'))

print('-------------------------------------------------------------------------------------------------------------')

# Module datetime:

import datetime

# Naive datetime - where the daylight saving zones and other specific things related to time zone are not considered.
# Aware datetime - to be aware of considering the specific things related to time zone we use this.

# Naive datetime
# datetime.date ( year, month and day) without (hours, minutes, seconds and microseconds)

d = datetime.date(2022, 12, 21)
print(d)

# To get the today's date.
d = datetime.date.today()
print(d)                    # To get today's date in YYYY-MM-DD format.
print(d.year)               # To get the year 
print(d.month)              # To get the month
print(d.day)                # To get today's day of the month.
print(d.weekday())          # To get the day of today, here Monday - 0, Sunday - 6
print(d.isoweekday())       # Monday - 1, sunday - 7

# To know the date of a week before and after today's date
dt = datetime.timedelta(days=7)
print(d - dt)
print(d + dt)

# date2 = date1 + timedelta
# timedelta = data1 + data2

# Number of days till my next birthday.
bday = datetime.date(2025, 4, 13)
till_bday = bday - d
print(till_bday)

# Number of seconds till my next birthday.
print(till_bday.total_seconds())

# datetime.time  will work with (hours, minutes, seconds and microseconds)
t = datetime.time(12, 34, 56, 12345)
print(t)                # output : 12:34:56.012345
print(t.hour)           # output : 12
print(t.minute)         # output : 34
print(t.second)         # output : 56

# datetime.datetime will work with (year, month, day, hours, minutes, seconds and microseconds)
dt = datetime.datetime(2025, 4, 13, 12, 54, 36, 1234)
print(dt)               # output : 2025-04-13 12:54:36.001234
print(dt.time())        # output : 12:54:36.001234
print(dt.date())        # output : 2025-04-13   
print(dt.hour)          # output : 12
print(dt.month)         # output : 4
print(dt.year)          # output : 2025
print(dt.minute)        # output : 54

td = datetime.timedelta(days=8)
print(dt + td)          # output : 2025-04-21 12:54:36.001234
td = datetime.timedelta(hours=14)
print(td + dt)          # output : 2025-04-14 02:54:36.001234
td = datetime.timedelta(minutes=567)
print(td + dt)          # output : 2025-04-13 22:21:36.001234
td = datetime.timedelta(seconds=34)
print(td+dt)            # output : 2025-04-13 12:55:10.001234

# Constructors in datetime module
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()                # Expects to take a timezone as the parameter.
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

