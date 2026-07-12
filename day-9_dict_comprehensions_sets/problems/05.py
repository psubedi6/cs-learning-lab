names = ["Alice", "Bob", "Charlie", "David", "Eve"]
"""expected:{
    "Alice": 5,
    "Charlie": 7,
    "David": 5
}"""
length = {value: len(value) for value in names if len(value)>3}
print(length)