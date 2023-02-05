'''
3.Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs)
'''

def solve(numheads, numlegs):
    chicken =  (4 * numheads - numlegs)//2
    rabbit = (numlegs - 2 * numheads)//2
    print(f"number of chickens = {chicken}")
    print(f"number of rabbits = {rabbit}")

heads = 35
legs = 94
solve(heads, legs)