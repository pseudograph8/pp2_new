'''
Implement a generator that returns all numbers from (n) down to 0.
'''

n = int(input())
gen = (i for i in range(n,-1,-1))
for i in gen:
    print(i)
