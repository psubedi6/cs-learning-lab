first_number = 10
second_number = 0

try:
    result = first_number / second_number
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide a number by zero.")