import pandas as pd
df = pd.read_json("./search_result.json")

print(df.groupby(['bloggername']).count())
