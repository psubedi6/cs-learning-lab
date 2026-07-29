languages = ["Python", "Java", "C++", "Go"]
for language in languages:
    print(f"{language}")

word = "Iterator"
for letter in word:
    print(letter)

animals = ["Dog", "Cat", "Rabbit"]
animal_iterator = iter(animals)
print(next(animal_iterator))
print(next(animal_iterator))
print(next(animal_iterator))


for i in range (5):
    print(i)