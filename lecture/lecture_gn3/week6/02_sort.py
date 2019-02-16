import pandas as pd
from libs.excelSaver import save

pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./195297.json")
print(df.count())

dfSorted = df.sort_values(['price'], ascending=[0])
dfTop10 = dfSorted.head(10)

save(dfTop10, 'priceTop10.xlsx')
