import os

print("Current working directory:", os.getcwd())
print("Writing to:", os.path.abspath("04.txt"))

with open("04.txt", "w") as f:
    f.write("Hello, World!\nWelcome to Python File I/O.")