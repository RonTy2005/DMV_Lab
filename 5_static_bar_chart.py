import matplotlib.pyplot as plt


categories = ['Math', 'Science', 'English', 'History', 'Computer']
marks = [85, 90, 78, 88, 95]


plt.figure(figsize=(7, 5))
plt.bar(categories, marks, color='blue')

plt.title("Student Marks Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.grid(axis='y')

plt.show()
