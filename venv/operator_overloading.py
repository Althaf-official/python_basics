class FUllNAME:
    def set_name(self,name):
        self.name=name

    def __add__(self, other):
        name=self.name+" "+other.name
        return name

#create two object for Fullname class
first_name=FUllNAME()
second_name=FUllNAME()

first_name.set_name("althaf")
second_name.set_name("mas")


full_name=first_name+second_name#this "+" is representing opertor overloading
print(full_name)