import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 14, 10, 18, 22, 19, 25, 17, 13, 16]

# Create box plot
plt.boxplot(data)

# Add title and labels
plt.title("Box Plot Example")
plt.ylabel("Values")

# Show plot
plt.show()