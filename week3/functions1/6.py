'''
6.Write a function that accepts string from user, 
return a sentence with the words reversed. 
We are ready -> ready are We
'''
def rev(s):
    s = reversed(s)
    print(*s)

sentence = list(input().split())
rev(sentence)

