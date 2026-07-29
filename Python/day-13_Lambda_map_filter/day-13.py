def double(number):
    return number * 2

def is_even(number):
    return number % 2 == 0

double_lambda = lambda number: number * 2

print(double(5))
print(double_lambda(5))

numbers = [1, 2, 3, 4, 5]
mapped_numbers = map(double, numbers)

mapped_list = list(mapped_numbers)
print(mapped_list)
lambda_map = list(map(lambda numbers:numbers*2, numbers))

even_numbers = filter(is_even, numbers)
lambda_filter = list(filter(lambda numbers: numbers%2==0, numbers ))
print(lambda_filter)