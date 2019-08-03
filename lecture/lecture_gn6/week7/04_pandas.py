import pandas as pd
pd.set_option('display.max_colwidth', -1)
# requests bs4 pandas
# pandas 데이터 분석
# 개수 세기, 합계, 평균, 표준편차
# dataframe -> 틀, 구조, 창문

df = pd.read_json("./coffee.json")
print(df.count())

print(df.head(5)[['price', 'link']])

dfSorted = df.sort_values(['price'])

print(dfSorted.head(5)[['price', 'link']])

print(dfSorted['price'])
print(dfSorted.head(5)[['price', 'link']])
print(dfSorted.tail(5)[['price', 'link']])



