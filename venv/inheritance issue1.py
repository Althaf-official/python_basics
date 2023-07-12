class First:
    def display(self):
        print("this is first class display function")

class Second:
    def display(self):
        print("this is second class display function")

#third class inherit first and second classes
#left right rule is here using
class Third(First,Second):
    def display_third(self):
        print("this is third class display funciton")


#create object for Third class
obj=Third()

#class first and second same name for function
obj.display()




