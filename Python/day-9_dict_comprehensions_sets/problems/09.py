numbers = [5, 10, 15, 20, 25, 30]
"""expected:{10, 20, 30}"""
num = {number for number in numbers if number%10==0}
print(num)