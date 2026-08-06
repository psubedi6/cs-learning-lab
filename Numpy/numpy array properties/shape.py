import numpy as np
arr_2d = np.array([[1,2,3],
                  [4,5,6]])
print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.dtype)

arr = np.array([1.2, 2.5, 3.8])
type =arr.astype(int)
print(type.dtype)

#operation
print(arr+5)
print(arr-5)
print(arr*5)
print(arr/5)

#aggratoion
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))