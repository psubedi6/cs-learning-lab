numbers = [1, 2, 3, 4, 5]
print(numbers)
words = ["ram", "hari", "sita", "gita"]
print(words)

print("square: " , [num * num for num in numbers])
print("double: " , [num * 2 for num in numbers])
print("add 10: " , [num + 10 for num in numbers])
print("uppercase: " , [word.upper() for word in words])
print("length: " ,[len(word) for word in words] )

print("even numbers:", [num for num in numbers if num % 2 == 0])
print("odd numbers:", [num for num in numbers if num % 2 != 0])
print("greater than 2:", [num for num in numbers if num > 2])
print("words longer than 3 letters:", [word for word in words if len(word) > 3])
print("words starting with s:", [word for word in words if word.startswith("s")])
print("square of even numbers:", [num * num for num in numbers if num % 2 == 0])