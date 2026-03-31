import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 20, np.nan, 40, 1000]  
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)


print("\nMissing Values:\n", df.isnull().sum())


df['Values'].fillna(df['Values'].mean(), inplace=True)


Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Replace outliers with median
median = df['Values'].median()
df['Values'] = np.where(
    (df['Values'] < lower_bound) | (df['Values'] > upper_bound),
    median,
    df['Values']
)

print("\nCleaned Dataset:\n", df)


plt.figure(figsize=(6, 4))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()


plt.figure(figsize=(6, 6))
plt.pie(df['Values'], labels=df['Category'], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()


plt.figure(figsize=(6, 4))
plt.step(df['Category'], df['Values'], where='mid', color='green')
plt.title("Stair Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()