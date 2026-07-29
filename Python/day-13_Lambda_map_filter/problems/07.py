names = ["Alice", "Bob", "Andrew", "Charlie", "Amanda", "David"]
#expected: ["Alice", "Andrew", "Amanda"]
starts_a = list(filter(lambda name: name.startswith("A") , names))
print(starts_a)