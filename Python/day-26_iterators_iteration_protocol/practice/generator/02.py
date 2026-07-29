def even_numbers():
    for num in range (1,11):
        if num%2 ==0:
            yield num

number = even_numbers()
for num in number:
    print(num)