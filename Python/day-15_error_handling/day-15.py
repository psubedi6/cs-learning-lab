try:
    print(10 / 0)
except:
    print("Something went wrong.")

try:
    print(10 / 0)

except ZeroDivisionError:
    print("You cannot divide by zero.")

#-----------------------------------------

try:
    print("A")
    print(10 / 0)
    print("B")

except ZeroDivisionError:
    print("C")

else:
    print("D")

finally:
    print("E")

print("F")


#------------------------------------------
try:
    print("A")

except ValueError:
    print("B")

else:
    print("C")

finally:
    print("D")