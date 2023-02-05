'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Note: don't use collection set.
'''

def unique(numbers):
    unique_list = []
    for item in numbers :
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
        

list = list(map(int, input().split()))
print(unique(list))