import pandas as pd
df = pd.read_json("./search_result.json")

print(df.columns)

df2 = df[['postdate', 'title', 'bloggername', 'link']]
df2Sorted = df2.sort_values(['postdate'], ascending=[0])
print(df2Sorted)
