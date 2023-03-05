"""
5. Write a Python program that matches a string that has an `'a'`
 followed by anything, ending in `'b'`.
"""
import re
str = input()

x = re.search(r'^a.*b$', str)

if x: 
    print("A match is found!")
else:
    print("Not matched!")