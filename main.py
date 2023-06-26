num1=int(input("enter two numbers"))
num2=int(input())


h="""this is
multi line 
comment
"""
print(type(num1))#this is sample comment
temp=num1
num1=num2
num2=temp

print("after swaping first num is :"  +str(num1)+"second number is "+str(num2))

print(h)
