import json
student= {
    "name": "Alice",
    "age": 20,
    "city": "Toronto"
}
with open("student06.json", "w") as f:
    json.dump(student, f, indent= 4)

print("File written successfully!")