import pandas as pd

departments = pd.read_csv("../data/departments.csv")
dept_emp = pd.read_csv("../data/dept_emp.csv")

merged = pd.merge(departments, dept_emp, on='dept_no')

merged.to_csv("../example/merge.csv")