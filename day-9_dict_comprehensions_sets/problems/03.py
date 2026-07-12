"""expected: {
    2: 4,
    4: 16,
    6: 36,
    8: 64
}"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
square = {value: value**2 for value in numbers if value%2==0}
print(square)