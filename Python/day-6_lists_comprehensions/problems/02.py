words = ["hi", "hello", "bye"]
#expected result : ['hi!', 'hello!', 'bye!']

result = [word+"!" for word in words]
print("The exclamation at end of list: ",result)