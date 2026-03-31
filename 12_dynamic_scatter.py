import matplotlib.pyplot as plt

x = []
y = []

print("Enter 5 values for X and Y:")

for i in range(5):
    x_value = float(input(f"Enter X value {i+1}: "))
    y_value = float(input(f"Enter Y value {i+1}: "))
    x.append(x_value)
    y.append(y_value)

# Create scatter plot
plt.figure(figsize=(6, 5))
plt.scatter(x, y, color='green', marker='o', s=100)

plt.title("Scatter Plot with 5 User Input Values")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.show()
