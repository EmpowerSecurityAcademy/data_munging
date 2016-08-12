import pandas as pd

departments = pd.read_csv("../data/departments.csv")
dept_emp = pd.read_csv("../data/dept_emp.csv")

merged = pd.merge(departments, dept_emp, on='dept_no')

aggregations = {
	
}

merged[merged['item'] == 'call'].groupby('').agg(aggregation)

merged.to_csv("../example/group_by.csv")