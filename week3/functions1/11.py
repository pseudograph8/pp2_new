'''Write a Python function that checks whether a word or phrase is palindrome or not. 
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam
'''

def isPal(str):
    return str == str[::-1]
        

s = input()
print(isPal(s))



