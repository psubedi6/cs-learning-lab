import numpy as np

#Broadcasting
p = np.array([100,200,300])
discont =10
final_price = p-(p* (discont/100))
print(final_price) 

#vectorization addition
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print((arr1 +arr2))

print((arr1 * arr2))