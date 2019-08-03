import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', 100)

# df = 표
df = pd.read_json("./coffee.json")
dfSorted = df.sort_values(['price'])
dfFiltered = dfSorted[(dfSorted['price'] >= 10000) & (dfSorted['price'] < 20000)]

print(dfFiltered[['price', 'link']])

