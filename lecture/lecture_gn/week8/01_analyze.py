#01_analyze.py
import pandas as pd

df = pd.read_json("./search_result.json")
print(df.count())

df.to_csv("./hello.csv", index=False)