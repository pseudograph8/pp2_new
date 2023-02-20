'''
Write a Python program to convert degree to radian.
'''

import math


degree = float(input("Input degree: "))
rad = math.radians(degree)
print("Output radian:", '%.6f' % rad)