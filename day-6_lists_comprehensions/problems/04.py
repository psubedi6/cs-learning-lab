words = ["sun", "planet", "moon", "galaxy", "sky"]
#expected result: ['planet', 'galaxy'] words that have more than 4 letters.
length_4= [letter for letter in words if len(letter)>4]
print(length_4)
