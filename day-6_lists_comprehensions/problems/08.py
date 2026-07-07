words = ["sun", "moon", "sky", "earth", "star"]
#expected result: ['MOON', 'EARTH', 'STAR'] length is greater than 3 uppercase
greater_upper = [word.upper() for word in words if len(word)>3 ]
print(greater_upper)