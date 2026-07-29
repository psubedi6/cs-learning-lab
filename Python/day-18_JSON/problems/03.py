import json

with open("student03.json", "r") as f:
    data = json.load(f)
print(data)
print(type(data))
print(data["name"])
print(data["age"])