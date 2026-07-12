names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

uppercase_names = {name: name.upper() for name in names}
print(uppercase_names)

long_names = {name: len(name) for name in names if len(name)> 3}
print(long_names)

student_marks = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 95
}

inverted = {value: key for key, value in student_marks.items()}
print(inverted)