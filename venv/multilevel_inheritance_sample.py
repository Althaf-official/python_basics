class First:
    def display_first(self):
        print("this is first class display function")

class Second(First):
    def display_second(self):
        print("this is second class display function")

#third class inherit first and second classes
class Third(Second):
    def display_third(self):
        print("this is third class display funciton")

"""
 multilevel inheritance refers to a scenario where a class inherits from another derived class, 
 which in turn inherits from its own base class. This creates a hierarchical structure of inheritance
"""


#create object for Third class
obj=Third()

#calling third class display function
obj.display_third()
obj.display_second()
obj.display_first()


print("_____________________________________________________________--")

#create object for second class
obj2=Second()

obj2.display_second()
obj2.display_first()

