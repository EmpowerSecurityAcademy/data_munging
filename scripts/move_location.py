import pandas as pd

imported = pd.read_csv("../data/departments.csv")

imported.to_csv("../tmp/departments.csv")