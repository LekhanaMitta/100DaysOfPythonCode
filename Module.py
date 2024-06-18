# June 18th 2024

# This file will be imported.
print('Importing the file...')

test = 'Test String'

def find_index(to_search, target):
    for i, val in enumerate(to_search):
        if val == target:
            return i
    return -1

    