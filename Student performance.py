# Student Performance Analytics Dashboard

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Sample Dataset
# -----------------------------
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Marks': [85, 72, 40, 90, 55, 30, 78],
    'Attendance': [92, 80, 60, 95, 70, 50, 88],
    'Logins': [40, 30, 10, 45, 20, 5, 35]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Average Calculation
# -----------------------------
avg_marks = df['Marks'].mean()
avg_attendance = df['Attendance'].mean()

print("Average Marks:", avg_marks)
print("Average Attendance:", avg_attendance)

# -----------------------------
# 3. Correlation Analysis
# -----------------------------
correlation = df[['Marks', 'Attendance', 'Logins']].corr()
print("\nCorrelation Matrix:\n", correlation)

# -----------------------------
# 4. Absentee Impact
# -----------------------------
low_attendance = df[df['Attendance'] < 75]
print("\nStudents with Low Attendance:\n", low_attendance)

# -----------------------------
# 5. Performance Classification
# -----------------------------
def classify(row):
    if row['Marks'] >= 75 and row['Attendance'] >= 85:
        return 'Top Performer'
    elif row['Marks'] < 50 or row['Attendance'] < 65:
        return 'At Risk'
    else:
        return 'Average'

df['Category'] = df.apply(classify, axis=1)

print("\nStudent Categories:\n", df)

# -----------------------------
# 6. Bar Chart: Top vs Struggling Students
# -----------------------------
category_count = df['Category'].value_counts()

plt.figure()
category_count.plot(kind='bar')
plt.title('Student Performance Categories')
plt.xlabel('Category')
plt.ylabel('Number of Students')
plt.show()

# -----------------------------
# 7. Heatmap: Correlation
# -----------------------------
plt.figure()
sns.heatmap(correlation, annot=True)
plt.title('Correlation Heatmap')
plt.show()

# -----------------------------
# 8. Bar Chart: Marks Comparison
# -----------------------------
plt.figure()
sns.barplot(x='Student', y='Marks', data=df)
plt.title('Marks of Students')
plt.show()
