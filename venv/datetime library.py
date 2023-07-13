import datetime

obj_day=datetime.datetime.now()

print(obj_day.strftime("%d/%m/%Y"))
print(datetime.datetime.today().month)
print(obj_day)
print(obj_day.time())
print(obj_day.now())
print(obj_day.astimezone())

