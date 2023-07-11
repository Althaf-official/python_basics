class firstClass():
    def __int__(self):
        print("First class init ")

    def set_name(self,name):
        self.name=name
        print("first class setname")

        #this is inheritance. second class inherit first class
        """
        It allows you to create a new class (known as the child class or subclass) based on an existing class (known as the parent class or superclass). 
        The child class inherits the attributes and methods of the parent class, and it can also add its own unique attributes and methods.
        """

        """"
super() is a built-in function that allows you to call methods from a parent class 
(also known as a superclass or base class) in your child class (also known as a subclass or derived class). 
It provides a way to invoke the methods of the parent class,
enabling you to reuse and extend the functionality defined in the parent class.
The super() function is primarily used within the __init__() method of a subclass to invoke the __init__() method of the parent class. 
By doing so, you can initialize the inherited attributes and perform any necessary setup defined in the parent class 
before adding or modifying attributes specific to the child class. This process is known as constructor chaining.
"""

class secondClass(firstClass):
    def __int__(self):
        super().__int__()
        print("Second class init ")

    def display_welcome(self):
        print("welcome to masgroup")

    def display_name(self):
        print(self.name)

    def set_name(self,name):
        super().set_name(name)
        print("second class is working setname")



secondobj=secondClass()
secondobj.display_welcome()
secondobj.set_name("althaf muhammed")
secondobj.display_name()

#overriding
secondobj.__int__()
secondobj.__int__()

"""
method overriding is a concept where a subclass provides a different implementation of a method that is already defined in its superclass. 
When a method in the subclass has the same name and parameters as a method in its superclass, 
the subclass method overrides the superclass method.

Method overriding allows you to customize the behavior of a method inherited from a superclass without modifying the original implementation
 in the superclass. This is achieved by redefining the method in the subclass with the desired implementation.
"""