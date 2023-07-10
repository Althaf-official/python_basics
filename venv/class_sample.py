#created a class
class My_Sample_Class():
    def sample_function(self,name):
        self.NAME=name

    def print_name(self):
        print(self.NAME)

"""
Self in Class
When defining a class in Python, methods (functions defined within the class) typically have self as their first parameter.
 This parameter is automatically passed by Python when the method is called on an instance of the class. 
 By convention, self is used as the name for this parameter, although you can technically choose any valid variable name.
"""



#created a object for class
x=My_Sample_Class()
y=My_Sample_Class()


my_wifes_name="jaseela asharaf is my wifes name"
my_name="Muhammed althaf is my name"


# call the function and passing aurument
x.sample_function(my_name)
y.sample_function(my_wifes_name)

#same function separate memory space
x.print_name()
y.print_name()
