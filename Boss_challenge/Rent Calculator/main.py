rent= int(input("Enter your flat rent: "))
food = int(input("Enter your total grocery"))
electricity_bill = int(input("Enter the electricity bill: "))
number_of_persons = int(input("Enter the number of person in flat: "))

average_bill = (rent+food+electricity_bill)/number_of_persons
print(f"Each person should pay: {average_bill}")