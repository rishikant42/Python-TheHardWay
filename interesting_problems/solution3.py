'''
According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards. 
("Semordnilap" is itself "palindromes" spelled backwards.) 
Write a semordnilap recogniser that accepts a file name (pointing to a list of words) 
from the user an d finds and prints all pairs of words that are semordnilaps to the screen. 
For example, if "stressed" and "desserts" is part of the word list, the the output should include the pair "stressed desserts". 
Note, by the way, that each pair by itself forms a palindrome! 
'''
def is_semordnilap(filename):
    File = open(filename)
    words = File.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results


if __name__ == "__main__":
    print is_semordnilap('semordnilap_words.txt')
