import datetime

end=datetime.datetime.now()
for i in range(20000):
    print(i)


now=datetime.datetime.now()

difference=end-now
print(difference)