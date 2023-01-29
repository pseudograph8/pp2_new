'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
Sets are unordered, so you cannot be sure in which order the items will appear.
'''
'''
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
'''
'''
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
'''
'''
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
If the item to remove does not exist, remove() will raise an error.
//
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
If the item to remove does not exist, discard() will NOT raise an error.
'''
'''
The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
'''
'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
'''
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
'''
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
'''
'''
Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
//
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
'''
'''
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)
'''

