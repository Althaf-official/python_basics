car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car)
x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print(car)