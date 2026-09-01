import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\Akanksha Patne\Downloads\employees.csv")
print(df.head())

average_salary = df["Salary"].mean()
print("Average Salary:", average_salary)

department_count = df["Department"].value_counts()
print(department_count)

high_salary = df[df["Salary"] > 50000]
print(high_salary)
high_salary.to_csv("high_salary_employees.csv", index=False)
print(high_salary)
