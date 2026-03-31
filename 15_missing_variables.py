import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    import seaborn as sns
    seaborn_available = True
except ImportError:
    seaborn_available = False

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'Marks': [85, 90, None, 88, 92]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)

print("\nMissing Values (True = Missing):\n")
print(df.isnull())

print("\nMissing Values Count per Column:\n")
print(df.isnull().sum())

print("\nTotal Missing Values in Dataset:", df.isnull().sum().sum())

print("\nRows with Missing Values:\n")
print(df[df.isnull().any(axis=1)])

if seaborn_available:
    plt.figure(figsize=(6, 4))
    sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
    plt.title("Missing Values Heatmap (Seaborn)")
    plt.show()

plt.figure(figsize=(6, 4))
plt.imshow(df.isnull(), cmap='viridis', aspect='auto')
plt.colorbar()
plt.title("Missing Values Heatmap (Matplotlib)")
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df)), df.index)
plt.show()