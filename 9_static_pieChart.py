import matplotlib.pyplot as plt


labels = ['Data Collection', 'Data Cleaning', 'Data Storage', 'Data Analysis', 'Data Visualization']
sizes = [20, 25, 15, 20, 20]  # Percentage distribution
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
explode = (0, 0.1, 0, 0, 0) 


plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', startangle=140, shadow=True)

plt.title('Data Management and Visualization Distribution')
plt.axis('equal') 

plt.show()
