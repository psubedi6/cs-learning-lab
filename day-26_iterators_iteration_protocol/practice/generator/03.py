def square_numbers(n):
    for num in range (1,n+1):
        yield num*num


n = square_numbers(6)

for num in n:
    print(num)