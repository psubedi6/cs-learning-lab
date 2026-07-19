
import json
student = {
    "city": "Toronto",
    "name": "Alice",
    "age": 20
}

with open("student07", "w") as f:
    json.dump(student, f, indent=4, sort_keys=True)