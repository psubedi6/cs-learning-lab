numbers = [1, 2, 3, 4, 5, 6]
#expected result: [1, 9, 25]odd numbers, and square them.
odd_sq = [num * num for num in numbers if num % 2 != 0]
print("The odd square is: ", odd_sq)