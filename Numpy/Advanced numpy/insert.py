import numpy as np

#insert in 1d
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)

#insert in 2d
arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_arr2d = np.insert(arr_2d, 1, [5,6], axis = None)
print(new_arr2d) 

#adding element at the end
arr2 = np.array([10,20,30])
print(np.append(arr2, [90,70, 80]))