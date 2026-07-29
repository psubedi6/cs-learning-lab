"""Create a dictionary called student with:
"name" → "Prakash"
"age" → 23
"city" → "Aurora"

Then:
change "age" to 24
change "city" to "Toronto"
print the whole dictionary"""

student = {
    "name": "Prakash",
    "age": 23,
    "city": "Aurora"
}
student["age"] = 24
student["city"]= "Toronto"
print(student)