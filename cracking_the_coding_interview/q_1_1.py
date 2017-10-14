'''
Created on Jan 30, 2017
@author: mbolaris
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

def is_unique(input_string):
    seen = [False] * 128
    for char in input_string:
        val = ord(char)
        if val > 128:
            print("Only ASCII strings supported")
            return False
        elif seen[val]:
            # Char already found in string
            return False
        seen[val] = True
    return True


