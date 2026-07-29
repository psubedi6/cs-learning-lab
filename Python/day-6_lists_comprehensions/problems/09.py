matrix = [[10, 20], [30, 40], [50, 60]]
#excepted result: [10, 20, 30, 40, 50, 60]
flattened = [num for row in matrix for num in row]
print(flattened)