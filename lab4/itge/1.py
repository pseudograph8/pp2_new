'''
Create a generator that generates the squares of numbers up to some number N.
'''

n = int(input())
'''
listt = [i**2 for i in range(1, n+1)]
print(listt)
'''

b = (i**2 for i in range(1, n))
for i in b:
    print(i)

    
