"""expected: {
    90: "Alice",
    80: "Bob",
    95: "Charlie"
}"""
student_marks = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 95
}
swapped = {value: key for key, value in student_marks.items()}
print(swapped)