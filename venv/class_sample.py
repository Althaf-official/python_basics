class MyClass:
    def __init__(self, name, age):#constructor
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


        """
        constructor is a special method within a class that is automatically called when you create an object of that class.
         It is used to initialize the attributes of the object. The constructor method is defined with the name __init__()
         
         """

# Creating an object of MyClass
obj = MyClass("John", 25)

# Calling the say_hello() method of the object
obj.say_hello()