#created a class
class My_Sample_Class():
    def sample_function(self,n):
        self.name=n

    def print_name(self):
        print(self.name)



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
