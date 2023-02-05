'''
Write a function that computes the volume of a sphere given its radius
'''
def volume(radius):
    print(4/3*(radius**3)*3.14)


r = int(input())
volume(r)