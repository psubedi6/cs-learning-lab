import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mping

x= np.linspace(0,5,11)
y = x**2

fig = plt.figure()
ax= fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y)
plt.show()
plt.savefig("basicplot.png")

img = mping.imread("images.jpg")
plt.axis("off")
plt.imshow(img)
cropped_image = img[50:200, 100:300]
plt.imshow(cropped_image)
plt.show()
 