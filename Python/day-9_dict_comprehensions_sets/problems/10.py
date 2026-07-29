student_marks = {
    "Alice": 90,
    "Bob": 65,
    "Charlie": 95,
    "David": 70,
    "Eve": 55
}
"""expected: {
    "Alice": 90,
    "Charlie": 95,
    "David": 70
}"""
highest = {
    name: mark
    for name, mark in student_marks.items()
    if mark >= 70
}
print(highest)