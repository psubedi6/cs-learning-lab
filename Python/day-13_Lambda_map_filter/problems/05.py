words = [
    "apple",
    "banana",
    "kiwi",
    "strawberry",
    "pear",
    "orange"
]
#expected:['banana', 'strawberry', 'orange']
greater_5= list(filter(lambda word: len(word)>5 , words))
print(greater_5)