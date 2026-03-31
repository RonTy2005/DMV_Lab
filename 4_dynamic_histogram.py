import matplotlib.pyplot as plt

data = []

n = int(input("Enter number of data values: "))

for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    data.append(value)

plt.hist(data, bins=10)
plt.xlabel("Data Values")
plt.ylabel("Frequency")
plt.title("Histogram from User Input")
plt.show()
