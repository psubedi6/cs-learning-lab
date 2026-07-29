import json

with open("student10.json", "r") as f:
    data = json.load(f)

for student in data:
        if student["id"]==2:
            student["age"] = 25

with open("student10.json", "w") as f:
         json.dump(data, f, indent=4)

print("Student updated successfully!")