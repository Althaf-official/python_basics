class firstClass():

    def set_name(self,name):
        self.name=name

        #this is inheritance. second class inherit first class
        """
        It allows you to create a new class (known as the child class or subclass) based on an existing class (known as the parent class or superclass). 
        The child class inherits the attributes and methods of the parent class, and it can also add its own unique attributes and methods.
        """
class secondClass(firstClass):

    def display_welcome(self):
        print("welcome to masgroup")

    def display_name(self):
        print(self.name)



secondobj=secondClass()
secondobj.set_name("althaf")
secondobj.display_name()