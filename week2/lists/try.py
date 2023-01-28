'''
list1 = ["abc", 34, True, 40, "male"]
'''
'''
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
'''
'''
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
'''
'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)
'''
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''

'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
The pop() method removes the specified index.
'''
'''
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
//
thislist = ["apple", "banana", "cherry"]
del thislist
'''
'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
//
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
'''
'''
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
'''
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
'''
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
'''
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fuits if "a" in x]

print(newlist)
'''
'''newlist = [x for x in fruits if x != "apple"]
   newlist = [x for x in range(10)]                '''


'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
'''
'''
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
'''
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
'''
'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
'''
'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
'''
'''
Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
'''