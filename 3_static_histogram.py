import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(75, 10, 200) # Mean=75, Std=10, n=200

plt.hist(scores, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Exam Scores")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")

plt.show()