def count():
    print("Start")

    yield 1

    print("Middle")

    yield 2

    print("End")

    
gen = count()
print(next(gen))
print(next(gen))