colors = ["red", "blue"]
items = ["shirt", "shoe"]
pairs_loop = []
for color in colors:
    for item in items:
        pairs_loop.append(f"{color} {item}")
print("pairs loop:", pairs_loop)

pairs_comp = [f"{color} {item}" for color in colors for item in items]
print("pairs comprehension:", pairs_comp)


matrix = [[1, 2], [3, 4], [5, 6]]
flat_loop = []
for row in matrix:
    for num in row:
        flat_loop.append(num)
print("flat loop:", flat_loop)

flat_comp = [num for row in matrix for num in row]
print("flat comprehension:", flat_comp)