class First:
    def display_first(self):
        print("this is first class display function")

class Second:
    def display_second(self):
        print("this is second class display function")

#third class inherit first and second classes
class Third(First,Second):
    def display_third(self):
        print("this is third class display funciton")


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

