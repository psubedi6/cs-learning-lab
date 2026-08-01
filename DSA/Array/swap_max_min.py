arr = [43,6,76,4,74,9]
maximum= float("-inf")
minimum= float("inf")

for i in range(len(arr)):
    if i> maximum:
        maximum = i
print(maximum)


for j in range(len(arr)):
    if j < minimum:
        minimum = j
print(minimum)

arr[maximum], arr[minimum]= arr[minimum], arr[maximum]
print(arr)