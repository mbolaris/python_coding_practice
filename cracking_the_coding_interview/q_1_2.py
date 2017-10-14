'''
Created on Jan 30, 2017
@author: mbolaris
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
'''

def is_permutation(string_a, string_b):
    if len(string_a) != len(string_b):
        return False
    
    char_counts = [0] * 128
    
    for char in string_a:
        char_counts[ord(char)] += 1
    
    for char in string_b:
        char_counts[ord(char)] -= 1
        if char_counts[ord(char)] < 0:
            return False
    
    return True        
    


