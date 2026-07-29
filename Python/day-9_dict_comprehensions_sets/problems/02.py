"""expected: {
    "Alice": "A",
    "Bob": "B",
    "Charlie": "C",
    "David": "D"
}"""
names = ["Alice", "Bob", "Charlie", "David"]
name ={ name: name[0] for name in names}
print(name)