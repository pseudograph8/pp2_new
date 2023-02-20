'''
Write a Python program to calculate the area of regular polygon.
'''
import math

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = (l**2*n)/(4*math.tan(math.pi/n))
print("The area of the polygon is:", int(area))