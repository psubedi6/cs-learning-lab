words = ["apple", "banana", "orange", "grape"]
"""expected:{
    "apple": "APPLE",
    "banana": "BANANA",
    "orange": "ORANGE",
    "grape": "GRAPE"
}"""
upper_words = {word: word.upper() for word in words}
print(upper_words)