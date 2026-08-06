import numpy as np
arr1= np.array([1,2,np.nan, 4, np.nan, 6])
#finding nan
print(np.isnan(arr1))

#replacing nan
replace = np.nan_to_num(arr1)
print(replace)

#finding infinite
arr2= np.array([1,2,np.inf, 4, -np.inf, 6])
print(np.isinf(arr2))

cleaned_inf = np.nan_to_num(arr2, posinf=1000, neginf= -1000)
print(cleaned_inf)