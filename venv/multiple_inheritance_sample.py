class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):
    def speak(self):
        return "Mammal: Roar!"


class Bird(Animal):
    def speak(self):
        return "Bird: Chirp!"


class Platypus(Mammal, Bird):
    pass



perry = Platypus("masss")
print(perry.name)  # Output: Perry
print(perry.speak())  # Output: Mammal: Roar!
"""
In the above example, we have three classes: Animal, Mammal, and Bird. 
The Animal class is a base class that provides a common name attribute and a speak method, which is left undefined.

The Mammal and Bird classes inherit from the Animal class and override the speak method to provide their own implementation.

The Platypus class inherits from both the Mammal and Bird classes using multiple inheritance. 
It doesn't define any additional methods or attributes.

When we create an instance of Platypus named perry, 
it inherits the name attribute from the Animal class and the speak method from the Mammal class. 
Therefore, calling perry.name returns "Perry", and perry.speak() returns "Mammal: Roar!".

Note that in the case of multiple inheritance, 
the order of the parent classes specified in the class definition matters. 
In our example, Platypus(Mammal, Bird), the Mammal class is listed first, 
so its speak method is the one that gets called. If we had specified Platypus(Bird, Mammal), 
the output would have been "Bird: Chirp!".

"""