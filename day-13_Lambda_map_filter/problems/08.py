words = [
    "madam",
    "apple",
    "level",
    "banana",
    "racecar",
    "python"
]
#expected: ["madam", "level", "racecar"] pallindrome
pal= list(filter(lambda word: word== word[::-1], words))
print(pal)