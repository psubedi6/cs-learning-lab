numbers = (100, 200, 300, 400, 500)
"""EXPECTED: 100
[200, 300, 400]
500"""
first, *middle, last = numbers
print(first)
print(middle)
print(last)