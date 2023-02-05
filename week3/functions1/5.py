'''
5.Write a function that accepts string from user and print all permutations of that string.
'''
from itertools import permutations

def perm(str):
    p = permutations(str)
    for i in p:
        print(i)

string = input()
perm(string)
