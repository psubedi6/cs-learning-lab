"""{
    key_expression : value_expression
    for variable in iterable
}"""
#expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

numbers= [1,2,3,4,5]
square = {value: value**2 for value in numbers}
print(square)