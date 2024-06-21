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

