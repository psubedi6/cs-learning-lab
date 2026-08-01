def linear_search(arr,target):
    for j in range (len(arr)):
        if arr[j] == target:
            return j
    return -1

arr = [4,2,7,8,1,2,5]
target = 8

index = linear_search(arr, target)
print(index)