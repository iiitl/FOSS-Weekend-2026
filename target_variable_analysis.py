import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("your_dataset.csv")  # change file name

# 2. Show columns
print("Columns:", df.columns)

# 3. Select target column (CHANGE THIS if needed)
target_column = "target"   # <-- change according to dataset

target = df[target_column]

# 4. Basic analysis
print("\nUnique values in target:")
print(target.unique())

print("\nNumber of classes:")
print(target.nunique())

# 5. Decide problem type
if target.nunique() == 2:
    print("\n👉 This is a BINARY CLASSIFICATION problem")
else:
    print("\n👉 This is a MULTI-CLASS CLASSIFICATION problem")

# 6. Value counts
print("\nClass distribution:")
print(target.value_counts())


#  GRAPH 1: Bar chart
plt.figure()
target.value_counts().plot(kind='bar')
plt.title("Target Class Distribution (Bar Chart)")
plt.xlabel("Classes")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()


#  GRAPH 2: Pie chart

plt.figure()
target.value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Target Class Distribution (Pie Chart)")
plt.ylabel("")
plt.show()


