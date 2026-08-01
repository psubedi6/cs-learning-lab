def swap(left, right):
    while left< right:
        arr[left], arr[right] = arr[right], arr[left]
        left +=1
        right -=1
    return arr

arr = [4,2,7,8,1,2,5]
swap(0,len(arr) - 1)
print(arr) 