import json
json_string = '{"name": "Alice", "age": 22, "city": "Toronto"}'
data = json.loads(json_string)
print(data)
print(data["name"])
print(type(data))
print(data["city"])