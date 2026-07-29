import json
with open("student09.json", "r") as f:
    data = json.load(f)

data["age"]= 21
del data["course"]

with open("student09.json", "w") as f:
    json.dump(data,f,indent=4)

print("Student updated successfully!")