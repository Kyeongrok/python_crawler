import pandas as pd

df = pd.read_json("./nangmyn.json")

print(df.count())