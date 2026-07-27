def countdown(n):
    for num in range(n+1,1):
        yield n

n = countdown(5)

for num in n:
    print(num)