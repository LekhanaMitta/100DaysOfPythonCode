# June 19th 2024
# File Object 
# create a file in the same directory, doesn't matter if it is text or other.

# Opening the file, and also specify if it used for read, write, updating
# Default - without any second argument reading is considered.
# 'r' - for reading
# 'w' - for writing
# 'a' - for appending to the file.

# open the file and read the file, we should explicitly close the file.
f = open('test.txt', 'r')
print(f.name)
# To read the contents of the opened text file.
print(f.read())
# we need to explicitly close the file when it's opened.
f.close()

# We use context manager to avoid explicitly closing the file, where it automatically closes the file when the code is exited.
with open('test.txt', 'r') as f:
    pass
# To know the mode of the file that is currently opened.
print(f.mode)

# To read the contents present in the file using context manager when we have a small file:
with open('test.txt', 'r') as f:
    contents = f.read()
    print(contents)
# output :
# Hi, This is test file.
# I am here to learn Python.
# By taking a 100 Days of Code challenge.

# To read the contents present in the file using context manager if it's a large file:
with open('test.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    # output :
    # ['Hi, This is test file.\n', 'I am here to learn Python.\n', 'By taking a 100 Days of Code challenge.']

# To read the contents present in the file line by line using context manager:
with open('test.txt', 'r') as f:
    contents = f.readline()
    print(contents, end = '')
    # output : Hi, This is test file.
    contents = f.readline()
    print(contents, end = '')
    # output : I am here to learn Python.

# To read the contents present in the file line by line without giving multiple readline() is:
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end = '')
        # output : 
        # Hi, This is test file.
        # I am here to learn Python.
        # By taking a 100 Days of Code challenge.

# To read a set of number of lines in read() function.
with open('test.txt', 'r') as f:
    contents = f.read()
    print(contents, end = '')
    # output : 
    # Hi, This is test file.
    # I am here to learn Python.
    # By taking a 100 Days of Code challenge.

# To read a set of characters from the file using read() function.
with open('test.txt', 'r') as f:
    contents = f.read(30)
    print(contents, end = '')
    # output :
    # Hi, This is test file.
    # I am he

with open('test.txt', 'r') as f:
    size_to_read = 10
    contents = f.read(size_to_read)
    while len(contents) > 0:
        print(contents, end='$')
        contents = f.read(size_to_read)
        # output :
        # Hi, This i$s test fil$e.
        # I am he$re to lear$n Python.
        # $By taking $a 100 Days$ of Code c$hallenge.$

# To go to any location we want we use seek() function.
with open('test.txt', 'r') as f:
    size_to_read = 10
    contents = f.read(size_to_read)
    print(contents, end = ' ')
    f.seek(0)
    contents = f.read(size_to_read)
    print(contents, end = ' ')
    # output : Hi, This iHi, This i

print('\n------------------------------------------------------------------------------------------------------------')

# Writing into a file.
# If we try to write into a file that is opened in the read mode then it throws error.
# UnsupportedOperation : Not writable error.
# If file doesn't exist then a new file of that name will be created.
# If file exists then the existing contents will be overwritten.
# To avoid overwriting the contents use append mode.

with open('test1.txt', 'w') as f:
    f.write('Test1')
    # Output : Test1
    f.seek(0)
    f.write('test1')
    # This overwrites the above Test1.
    # output : test1
    f.seek(0)
    f.write('R')
    # This overwrites only the no. of characters that are present in the write function.
    # output : Rest1

print('------------------------------------------------------------------------------------------------------------')

# Both reading and writing operation on the same file.
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# Trying to write a jpg file into other using 'r' and 'w' modes.
# with open('image.jpg', 'r') as rf:
#     with open('image_copy.jpg', 'w') as wf:
#         for line in rf:
#             wf.write(line)
# This gives UnicodeDecodeError because .txt contains the data in UTF-8 format while jpg contains in byte format.

# Writing a jpg file into other jpg file using 'rb', 'wb'
with open('image.jpg', 'rb') as rf:
    with open('image_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        b_contents = rf.read(chunk_size)
        while len(b_contents) > 0:
            wf.write(b_contents)
            b_contents = rf.read(chunk_size)

print('------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------')