'''
Created on Jan 30, 2017
@author: mbolaris
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

def is_unique(input_string):
    seen = [False] * 256
    for char in input_string:
        val = ord(char)
        if seen[val]:
            # Char already found in string
            return False
        seen[val] = True
    return True


