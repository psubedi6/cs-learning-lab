def add_numbers(*args):
    total = 0
    for num in args:
        total = total+num
    print(f"The sum of {args} is {total}")
add_numbers(5,10)
add_numbers(1,2,3,4)
add_numbers(100,200,300)