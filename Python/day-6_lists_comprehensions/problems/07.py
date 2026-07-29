words = ["ball", "cat", "bat", "apple", "banana", "dog"]
#expected result: ['ball', 'bat', 'banana']words start with letter "b"
starts_b = [word for word in words if word.startswith("b")]
print("starts with b: ", starts_b)