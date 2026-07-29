import json
student = {
    "name": "Alice",
    "age": 20,
    "address": {
        "city": "Toronto",
        "province": "Ontario"
    },
    "courses": [
        "Python",
        "Data Science",
        "SQL"
    ]
}
with open ("student08.json", "w") as f:
    json.dump(student, f, indent=4)

with open ("student08.json", "r") as f:
    data = json.load(f)
    print(data["name"])
    print(data["address"]["city"])
    print(data["address"]["province"])
    print(data["courses"][0])
    print(data["courses"][2])  