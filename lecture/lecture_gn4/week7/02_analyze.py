import pandas as pd

df = pd.read_json("./macaron.json")
print(df.count())