import matplotlib.pyplot as plt

x= [1, 2, 3, 4]
y= [10, 20, 15, 25]

plt.subplot(1,2,1)#firsr row, 2nd column, 1st subplot
plt.plot(x,y)
plt.title("Line chart")

plt.subplot(1,2,2)#firsr row, 2nd column, 3nd subplot
plt.bar(x,y)
plt.title("Line chart")
plt.show()


fig, ax= plt.subplots(1,2,1)

ax[0].plot(x,y, color ="blue")
ax[0].set_title("Line plot")

ax[1].bar(x,y, color = "green")
ax[1].set_title("Bar chart")

plt.tight_layout() 
plt.show()



plt.plot(x,y, color = "blue", marker= "o", )
plt.title("Simple Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.savefig("line_plot.png", dpi = 300, bbox_inches="tight")
plt.show()