import matplotlib.pyplot as plt

x=[]
y=[]

n= int(input("Enter number of points: "))

for i in range(n):
    xi = int(input(f"Enter x[{i}]: "))
    yi = int(input(f"Enter y[{i}]: "))
    x.append(xi)
    y.append(yi)

plt.plot(x, y, marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Dynamic Line Chart (User Input)")
plt.grid(True)
plt.show()