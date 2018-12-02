import pandas as pd

df = pd.read_json("./search_result.json")
print(df.count())
print(df['postdate'])
df['postdate'] = pd.to_datetime(df['postdate'], format="%Y%m%d")

print(df['postdate'])
