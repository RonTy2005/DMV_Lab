import matplotlib.pyplot as plt

# Ask user for number of bars
n = int(input("Enter the number of categories: "))

categories = []
values = []

# Get category names and values from user
for i in range(n):
    category = input(f"Enter name of category {i+1}: ")
    value = float(input(f"Enter value for {category}: "))
    categories.append(category)
    values.append(value)

# Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='teal')

plt.title("Bar Chart from User Input")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.grid(axis='y')

plt.show()
