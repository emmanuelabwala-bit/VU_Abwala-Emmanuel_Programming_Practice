# Topic 6: NumPy, Pandas, Matplotlib and Seaborn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print(numbers)

# 2. NumPy calculations
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
print(np.sum(numbers))

# 3. NumPy matrix
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)
print(matrix.shape)

# 4. Pandas DataFrame
data = {
    "Name": ["John", "Mary", "Peter"],
    "Age": [20, 22, 21],
    "Score": [80, 75, 90]
}

df = pd.DataFrame(data)

print(df)

# 5. Selecting columns
print(df["Name"])
print(df["Score"])

# 6. Basic data analysis
print(df.head())
print(df.info())
print(df.describe())

# 7. Reading a CSV dataset
# Put a file named students.csv in the same folder, then use:
#
# df = pd.read_csv("students.csv")
# print(df)

# 8. Filtering data
result = df[df["Score"] > 70]
print(result)

# 9. Matplotlib line graph
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Over Time")
plt.show()

# 10. Matplotlib bar chart
names = ["John", "Mary", "Peter"]
scores = [80, 70, 90]

plt.bar(names, scores)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# 11. Seaborn histogram
values = [10, 20, 20, 30, 30, 30, 40, 50]

sns.histplot(values)
plt.title("Distribution of Values")
plt.show()

# 12. Seaborn with Pandas
gender_data = {
    "Gender": ["Male", "Female", "Male", "Female", "Male"],
    "Score": [70, 80, 75, 90, 85]
}

gender_df = pd.DataFrame(gender_data)

sns.barplot(data=gender_df, x="Gender", y="Score")
plt.title("Average Score by Gender")
plt.show()
