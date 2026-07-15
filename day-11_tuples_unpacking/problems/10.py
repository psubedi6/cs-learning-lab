numbers = 10, 20, 30, 40, 50, 20
"""Todo:
Print the first element.
Print the last element.
Print the slice:
(20, 30, 40)
Print how many times 20 appears.
Print the index of 40.
Use starred unpacking to create:
first
middle
last
Print:
first
middle
last
"""
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers.count(20))
print(numbers.index(40))
first,*middle,last = numbers
print(first)
print(middle)
print(last)
