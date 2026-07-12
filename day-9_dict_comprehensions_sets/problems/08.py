names = ["Alice", "Bob", "Andrew", "Charlie", "Amanda"]
"""expected:{
    "Alice": 5,
    "Andrew": 6,
    "Amanda": 6
}"""
length = {name: len(name) for name in names if len(name)>3 }
print(length)