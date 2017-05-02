import random

def matched(str):
    count = 0
    for i in str:
        if i == "[":
            count += 1
        elif i == "]":
            count -= 1
        if count < 0:
            return False
    return count == 0

def generate_string(n):
    '''returns a string with n opening ("[") and n closing brackets ("]")'''
    string = ["[", "]"] * n
    random.shuffle(string)
    #print("".join(string))
    return "".join(string) 

print matched(generate_string(2))
