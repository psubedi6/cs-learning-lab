import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
#add or concatinatte
new_arr = np.concatenate((arr1,arr2))
print(new_arr)


#removing 1d
arr = np.array([10,20,30,40,50,60])
new_arr_remove = np.delete(arr, 0)
print(new_arr_remove)

#removing 2D

twoD_arr = np.array([[1,2,3],[4,5,6]])
new_arr_2d = np.delete(twoD_arr, 0 , axis= 1)
print(new_arr_2d)