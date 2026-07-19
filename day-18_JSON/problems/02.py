import json
student = {
    "name": "Bob",
    "age": 20,
    "course": "Computer Science"
}
json_string = json.dumps(student)
print(json_string)
print(type(json_string))