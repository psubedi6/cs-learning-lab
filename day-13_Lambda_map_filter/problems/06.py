numbers = [-5, 10, -3, 7, 0, -8, 15]
#expected: [10, 7, 15] 
positive= list(filter(lambda number: number>0, numbers))
print(positive)