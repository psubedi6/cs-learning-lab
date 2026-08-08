import matplotlib.pyplot as plt
#bargraph
product= ["A", "B","C","D"]
sales = [1000,1500,800,1200]

plt.barh(product, sales, color ="orange", label= "Sales 2025")
plt.xlabel("Product"), plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend()
plt.show()

#piechart
regions = ["North", "South", "East", "West"]
revenue = [3000,2000,1500,1000]
plt.pie(revenue, labels= regions, autopct= "%1.1f%%",colors = ["gold", "skyblue", "lightgreen", "coral"])
plt.title("Revenue contribution by percentage")
plt.show()

#histogram
scores = [45,67,23,54,87,45,34,67,87,23,98,45,3,7,98,54,65,64]
plt.hist(scores, bins= 10, color="purple", edgecolor= "black")
plt.xlabel("Score Range"), plt.ylabel("Number of students")
plt.title("Score distribution of students")
plt.show()

#scatter plots
hours_studied = [1,2,3,4,5,6,7,8]
exam_scores = [50, 55, 70, 75, 80, 85, 90, 95]
plt.scatter(hours_studied, exam_scores, color= "green", marker="o", label = "Student data")
plt.xlabel = ("Hours studied")
plt.ylabel = ("Exam score")
plt.title("Relationship between study time and exam score")
plt.legend(), plt.grid(True)
plt.show()

#mersing 2 scatters
hours_studied = [1,2,3,4,5,6,7,8]
exam_scores = [50, 55, 70, 75, 80, 85, 90, 95]
plt.scatter(hours_studied, exam_scores, color= "green", marker="o", label = "Student data")

plt.scatter([1,2,3],[50,55,60], color="blue", label = "Class A")
plt.scatter([1,2,3],[45,50,52], color="orange", label = "Class B")

plt.xlabel = ("Hours studied")
plt.ylabel = ("Exam score")
plt.title("Relationship between study time and exam score")
plt.legend(), plt.grid(True)
plt.show()