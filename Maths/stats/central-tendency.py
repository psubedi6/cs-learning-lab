#Mean: average
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
#Mean: average
arr = np.array([50,60,70,80,90])
arr2= np.array([100,120,150,9000,5000])
print(np.mean(arr))
print(np.mean(arr2))

#Median: middle value
arr3= np.array([100,120,150,9000,5000])
print(np.median(arr3))

#mode: most appearing value
arr4= np.array([100,120,150,9000,5000])
print(stats.mode(arr4))


#variance
data= [10,20,30]
print(np.var(data))

#Standard deviation
arr5= [10,30,50,70,90]
print("Mean", np.mean(arr5))
print("STD", np.std(arr5))

#Data visualization
arr6=[10,20,20,30,30,30,40,50]
plt.hist(arr6)
plt.show()

plt.bar(["a","b","c","d","e","f","g","h"],arr6)
plt.show()

#Probability
