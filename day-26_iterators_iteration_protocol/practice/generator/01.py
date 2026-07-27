def count_to_three():
    yield 1
    yield 2
    yield 3 
count = count_to_three()
print(next(count))
print(next(count))
print(next(count))