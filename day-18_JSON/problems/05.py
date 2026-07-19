import json

with open("student05.json","r") as f:
    data = json.load(f)

data["age"]= 22
data["country"] = "Canada"

with open("student05.json", "w") as f:
    json.dump(data,f,indent =4)
print("Student information updated successfully!")