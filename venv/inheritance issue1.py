class First:
    def display(self):
        print("this is first class display function")

class Second:
    def display(self):
        print("this is second class display function")

#third class inherit first and second classes
#left right rule is here using
class Third(First,Second):#left-to-right order
    def display_third(self):
        print("this is third class display funciton")


#create object for Third class
obj=Third()

#class first and second same name for function
obj.display()

"""
multiple inheritance allows a class to inherit attributes and methods from multiple base classes.
 When multiple inheritance is used and two or more base classes define a method with the same name, 
 it can lead to a situation called "Diamond Problem" or "Ambiguity Problem."
"""


print(Third.mro())

"""
In Python, the MRO is determined by the C3 linearization algorithm. It follows a depth-first, left-to-right order
"""
