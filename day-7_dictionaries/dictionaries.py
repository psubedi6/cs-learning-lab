student = {
    "name": "Prakash",
    "age": 23,
    "city": "Aurora"
}
print(student)
print(student["name"])
print(student["age"])
print(student["city"])
student["age"] = 24
student["city"] = "Toronto"

print(student)
print(student["age"])
student["country"] = "Canada"
student["course"] = "Computer Science"

print(student)
print(student["country"])
print(student["course"])

del student["country"]
removed_course = student.pop("course")
print(student)
print(removed_course)

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))
print(student.get("email"))
print(student.get("email", "No email found"))


student_profile = {
    "name": "Prakash",
    "age": 24,
    "address": {
        "city": "Toronto",
        "province": "Ontario",
        "country": "Canada"
    }
}
print(student_profile)
print(student_profile["address"])
print(student_profile["address"]["city"])

