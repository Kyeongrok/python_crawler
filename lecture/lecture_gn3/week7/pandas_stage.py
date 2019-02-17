import pandas as pd
import numpy as np
from libs.excelSaver import save

df = pd.read_json("./products.json")
df['price'] = df['price'].str.replace(',', '').astype(float)
print(df['price'])

print(df.columns)
# sorted
dfSorted = df.sort_values(['price'])
dfSorted['rank'] = np.arange(1, len(df)+1)
# price top5
dfPriceTop5 = dfSorted.head(5)

# price reverse top 5
dfPriceReverseTop5 = df.sort_values(['price'], ascending=[0]).head(5)

print("av:", df['price'].mean())
print("std:", df['price'].std())
print("var:", df['price'].var())

d = {'col1': df['price'].mean(), 'col2':[]}
dfResult = pd.DataFrame(data=d)

# 1개의 엑셀 파일에 저장
dfs = [
    {"df":dfSorted, "sheetName":"sorted"},
    {"df":dfPriceTop5, "sheetName":"priceTop5"},
    {"df":dfPriceReverseTop5, "sheetName":"priceReverseTop5"},
    {"df":dfResult, "sheetName":"dfResult"}

]
save(dfs, "./productAnalyze.xlsx")





