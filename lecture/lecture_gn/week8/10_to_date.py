import pandas as pd

df = pd.read_json("./search_result.json")
# print(df['postdate'])

df2 = df[df['postdate'] != '']
df2['postdate'] = pd.to_datetime(df2['postdate'], format="%Y%m%d")



