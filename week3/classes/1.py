'''1. Define a class which has at least two methods: getString: to get a string from console input 
printString: to print the string in upper case.'''

class myClass(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input() # this function asks for input
    def printString(self):
        print (self.s.upper()) #this function changes to upper case


strObj = myClass()  # this initialises the class 
strObj.getString() # this asks for a string 
strObj.printString() #this prints the string in upper case 

