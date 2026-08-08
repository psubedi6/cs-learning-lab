import matplotlib.pyplot as plt

months= [1,2,3,4]
sales = [100,1500,1200,1800]

plt.plot(months, sales, color = "green", linestyle="--", linewidth = 2,marker = "h", label="2025 sales data")
plt.title("Monthly Sales Data Report")
plt.xlabel("Months"), plt.ylabel("Sales")
plt.legend(fontsize= 10)
plt.grid(color = "grey", linestyle = ":", linewidth = 1)
plt.xlim(1,6),plt.ylim(0,2000)
plt.xticks([1,2,3,4,5], ["Month1","Month2","Month3","Month4","Month5"])
plt.show()