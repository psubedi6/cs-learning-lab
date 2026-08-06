import numpy as np

arr = np.array([10,20,30,40,55])

#one element
print(arr[0])
print(arr[0:2])
print(arr[-1])

#multiple element
print(arr[0:9])

#fancy indexing
print(arr[[0,2,4]])


#filtering
print(arr[arr>25])

#reshaping
arr1 = np.array([1,2,3,4,5,6])
print(arr1.reshape(2,3))
print(arr1.ravel())
print(arr1.flatten())