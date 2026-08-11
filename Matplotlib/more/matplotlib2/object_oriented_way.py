import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(0,5,11)
y = x**2

fig = plt.figure()

axis1= fig.add_axes([0.5,0,0.5,0.5])
axis1.plot(x,y)


axis2= fig.add_axes([0,0.5,0.5,0.5])
axis2.plot(y,x)

plt.show()