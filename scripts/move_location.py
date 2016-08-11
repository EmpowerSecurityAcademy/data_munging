import pandas as pd

# move the departments

imported = pd.read_csv("../data/departments.csv")

imported.to_csv("../example/departments.csv")