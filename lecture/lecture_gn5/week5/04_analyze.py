# .json을 pandas로 불러와서 개수 세기
import pandas as pd

df = pd.read_json("./bodywash.json")
df = df[['price', 'link']]

print(df.count())

dfSorted = df.sort_values(['price'])
print(dfSorted.head(10))
print(dfSorted.tail(10))
print(type(dfSorted['price'][0]))


