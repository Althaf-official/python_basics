car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

print(car.get("color"))
print(car.get("model"))

print("after pop")
car.pop("model")
print(car.get("model"))