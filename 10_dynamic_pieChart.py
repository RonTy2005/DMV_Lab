import matplotlib.pyplot as plt


n = int(input("Enter the number of categories: "))

labels = []
sizes = []


for i in range(n):
    label = input(f"Enter name of category {i+1}: ")
    value = float(input(f"Enter value for {label}: "))
    labels.append(label)
    sizes.append(value)


plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("User Input Based Pie Chart")
plt.axis('equal')  

plt.show()
