import pandas as pd
import matplotlib.pyplot as plt

# Read data from files
df_2020 = pd.read_csv('2020input2.csv', delim_whitespace=True, header=None, names=['Xleft', 'Xright', 'Count'])
df_2024 = pd.read_csv('2024input2.csv', header=None, names=['Grades'])

df_2020.head()

df_2024.head()

# Calculation 2020
# Calculate midpoint of intervals from 2020 exam dataframe
midpoints = (df_2020['Xleft'] + df_2020['Xright']) / 2
tot_students_2020 = sum(df_2020['Count'])
M_2020 = sum((midpoints * df_2020['Count'])) / tot_students_2020
S_2020 = (sum(((midpoints - M_2020) ** 2) * df_2020['Count']) / tot_students_2020) ** 0.5

# Calculation 2024
M_2024 = df_2024["Grades"].sum() / len(df_2024["Grades"])
S_2024 = ((((df_2024["Grades"] - M_2024) ** 2).sum()) / len(df_2024["Grades"])) ** 0.5

# Calculate V proportion of students with grade below 25 in 2024 exam
count = sum(grade < 25 for grade in df_2024['Grades'])
V = count / len(df_2024['Grades'])

# Plotting histogram
plt.figure(figsize=(12, 8))
plt.hist(midpoints, bins=range(0,101,4), weights=df_2020['Count'], alpha=0.5, label='Exams Year 2020',color = 'coral',edgecolor='black')
plt.hist(df_2024['Grades'], bins=range(0,101,4), alpha=0.5, label='Exams Year 2024',color = 'cyan',edgecolor='black')

# Plot mean for both distributions
plt.axvline(M_2020, color='red', linestyle='dashed', linewidth=1, label='Mean 2020')
plt.axvline(M_2024, color='blue', linestyle='dashed', linewidth=1, label='Mean 2024')

plt.text(0.96, 0.97, f'Mean 2020: {M_2020:.2f}\nStd.Dev. 2020: {S_2020:.2f}\nMean 2024: {M_2024:.2f}\nStd.Dev. 2024: {S_2024:.2f}\nV: {V:.2g}, ha='right', va='top', transform=plt.gca().transAxes)
plt.xlabel('Grades')
plt.ylabel('Count of Students')
plt.title('Distribution of Grades in 2020 and 2024 Exams')
plt.legend(loc='upper left')

plt.savefig('figure.png')

plt.show()