numbers = (10, 20, 30)
print(numbers)


a = (5)
b = (5,)
print(type(a))
print(type(b))


numbers = (10, 20, 30)
numbers_without_parentheses = 10, 20, 30
empty = ()
single = (5,)
student = ("Prakash", 24, True, 3.8)
nested = ("Marks", (85, 90, 95))
print(numbers)
print(numbers_without_parentheses)
print(empty)
print(single)
print(student)
print(nested)


numbers = (10, 20, 30)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[-1])
print(numbers[-2])
print(numbers[-3])


numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])
print(numbers[::2])
print(numbers[1::2])


person = ("Prakash", 24, "Canada")
name, age, country = person
print(name)
print(age)
print(country)


numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(first)
print(middle)
print(last)