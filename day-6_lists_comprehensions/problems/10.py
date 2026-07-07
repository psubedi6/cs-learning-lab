words = ["pen", "notebook", "eraser", "ink", "marker"]
result = []
for word in words:
    if len(word) > 3:
        result.append(word.upper())
print("loop result:", result)
#expected result: ['NOTEBOOK', 'ERASER', 'MARKER'] with list comprehension

comp= [word.upper() for word in words if len(word)>3]
print("loop result: ", comp)