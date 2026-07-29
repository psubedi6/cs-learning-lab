fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[-3:])
print(fruits[:-1])

numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[-2:])
print(numbers[:-1])

fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

fruits = ["apple", "banana"]
fruits.extend(["mango", "orange"])
print(fruits)

fruits1 = ["apple", "banana"]
fruits1.append(["mango", "orange"])
print(fruits1)
fruits2 = ["apple", "banana"]
fruits2.extend(["mango", "orange"])
print(fruits2)

fruits = ["apple", "banana", "mango", "orange"]
fruits.remove("banana")
print(fruits)
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
print(numbers)

fruits = ["apple", "banana", "mango", "orange"]
fruits.pop(1)
print(fruits)
fruits = ["apple", "banana", "mango", "orange"]
removed_item = fruits.pop(1)
print(removed_item)
print(fruits)
fruits = ["apple", "banana", "mango", "orange"]
fruits.pop()
print(fruits)

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

fruits = ["apple", "banana", "mango", "orange"]
fruits.reverse()
print(fruits)

fruits = ["mango", "apple", "orange", "banana"]
fruits.sort()
print(fruits)

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)