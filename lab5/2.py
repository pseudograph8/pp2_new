"""
2. Write a Python program that matches a s
tring that has an `'a'` followed by two to three `'b'`.
"""
import re
txt = input()
x = re.search(r'ab{2,3}',txt)

print(x)