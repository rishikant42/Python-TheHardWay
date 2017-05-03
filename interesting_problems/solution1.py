#!/usr/bin/python

'''
Generate a string with N opening brackets ("[") and N closing brackets ("]"), in some arbitrary order. 
Determine whether the generated string is balanced; that is, 
whether it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest. 
'''

import random

def balanced_parentheses(string):
    '''check whether input string have balanced parentheses'''
    count = 0
    for i in string:
        if i == "[":
            count += 1
        elif i == "]":
            count -= 1
        if count < 0:
            return "NOT OK"
    if count == 0:
        return "OK"
    else:
        return "NOT OK"

def generate_string(n):
    '''returns a string with n opening ("[") and n closing brackets ("]")'''
    string = ["[", "]"] * n
    random.shuffle(string)
    return "".join(string) 

def test():
    for i in range(1,5):
        input_str = generate_string(i)
        output = balanced_parentheses(input_str)
        print "Input:", input_str
        print "Output:", output
        print ""

if __name__ == "__main__":
    test()
