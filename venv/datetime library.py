import datetime

x=datetime.datetime(1995,12,27)
y=datetime.datetime.now()
print(y)
print(x)


diff=y-x;
print("i live total  :"+str(diff.days)+" Days")

years=diff.days/365
print("My age is   : "+str(years))

