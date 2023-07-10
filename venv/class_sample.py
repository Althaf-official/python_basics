#created a class
class My_Sample_Class():
    def sample_function(self,name,age,birth_year):
        self.NAME=name
        self.AGE=age
        self.BIRTH_YEAR=birth_year
    def print_name(self):
        #print(self.NAME)
        #print(self.AGE)
        print(f"my name is {self.NAME} and  age is {self.AGE}. birth year is {self.BIRTH_YEAR}")


"""
Self in Class
When defining a class in Python, methods (functions defined within the class) typically have self as their first parameter.
 This parameter is automatically passed by Python when the method is called on an instance of the class. 
 By convention, self is used as the name for this parameter, although you can technically choose any valid variable name.
"""


#created a object for class
x=My_Sample_Class()
y=My_Sample_Class()


my_wifes_name="jaseela asharaf"
my_name="Muhammed althaf"



# call the function and passing aurument
x.sample_function(my_name,age=27,birth_year=1995)
y.sample_function(my_wifes_name,age=21,birth_year=2001)

#same function separate memory space
x.print_name()
y.print_name()
