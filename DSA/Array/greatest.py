arr = [11,64,81,1,9,99]
maxi = float("-inf")

for i in arr:
    if i> maxi:
        maxi=i
        
print(f"The greatest number is: {maxi}")

for j in range(len(arr)):
    if arr[j] == maxi:
        print(f"The index of {maxi} is {j}")