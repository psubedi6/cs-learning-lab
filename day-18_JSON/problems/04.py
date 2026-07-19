import json
with open("student04.json", "w") as f:
    writing = json.dump("student04",f)
print("data written successfully")