import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))


ax1.plot(x, y1, marker='o', color='blue')
ax1.set_title("Line Chart 1")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("Y-axis")
ax1.grid(True)


ax2.bar(x, y2, color='orange')
ax2.set_title("Bar Chart 2")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Y-axis")
ax2.grid(True)

plt.tight_layout()  
plt.show()
