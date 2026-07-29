numbers = [1, 2, 3, 4, 5]
squares_loop = []
for num in numbers:
    squares_loop.append(num * num)
print("loop:", squares_loop)
print("comprehension: ", [num * num for num in numbers])


even_loop = []
for num in numbers:
    if num % 2 == 0:
        even_loop.append(num)
print("even loop:", even_loop)
even_num = [num for num in numbers if num%2==0]
print("comprehension_even", even_num)


even_square_loop = []
for num in numbers:
    if num % 2 == 0:
        even_square_loop.append(num * num)
print("even square loop:", even_square_loop)
even_sq = [num * num for num in numbers if num % 2 == 0]
print(even_sq)