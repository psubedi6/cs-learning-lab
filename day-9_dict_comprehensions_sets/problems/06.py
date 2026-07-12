words = ["apple", "banana", "apple", "orange", "banana", "grape"]
#expected: {"apple", "banana", "orange", "grape"}

sets = {word for word in words}
print(sets)