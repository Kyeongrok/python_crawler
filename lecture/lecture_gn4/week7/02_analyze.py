import pandas as pd
from libs.singleExcelSaver import save

df = pd.read_json("./macaron.json")

# save(df, "macaron.xlsx")

# 내림차순 정렬해서 xlsx로 저장해보세요.
dfSorted = df.sort_values(by=['price'], ascending=False)

# save(dfSorted, "macaron.xlsx")
# print(dfSorted.head(10))

# 가격대 10000이상 20000이하
dfBetween = dfSorted[dfSorted['price'] >= 10000]
dfBetween2 = dfSorted[(dfSorted['price'] >= 10000) & (dfSorted['price']<=20000)]

tastes = ['초코', '민트', '딸기', '오렌지', '블루베리']
for taste in tastes:
    dfFilter = df[df['name'].str.contains(taste)]
    print(dfFilter[['name', 'price']])
