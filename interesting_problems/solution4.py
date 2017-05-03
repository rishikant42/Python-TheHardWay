'''
Write a program that wil l calcul ate the average word length of a text stored in a file 
(i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens). 
'''
import re

def avg_word_length(filepath):
    file = open(filepath)
    words = re.findall('\w+', file.read())
    total_length = 0.0
    for word in words:
        total_length += len(word)

    return total_length / len(words)

if __name__ == "__main__":
    print "Average word length:", avg_word_length('file.txt')
