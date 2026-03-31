import matplotlib.pyplot as plt


x = [10, 20, 30, 40, 50]
y = [15, 25, 35, 45, 30]


plt.figure(figsize=(6, 5))
plt.scatter(x, y, color='blue', marker='o', s=100)

plt.title("Scatter Plot with 5 Values")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()
