import pandas as pd
from libs.excelSaver import save

df = pd.read_json("./result.json")
print(df.count())

# 가격이 가장 비싼 제품, 가격이 가장 싼 제품
df = df.sort_values(['price'], ascending=[0])
print(df.columns)
print(df['name'])

# 매일유업 - 경쟁자 분석, 우리들이 마케팅 잘 하고 있나
# name에 우유가 포함되어 있는 데이터만 뽑아보세요.
# how to filter include some word pandas
# 특정 단어가 포함되어 있는 데이터 필터링 하기
drinks = ["우유", "두유", "커피", "라떼" "콜라", "오렌지", "수"]

for drink in drinks:
    resultDf = df[df['name'].str.contains(drink)]
    save(resultDf, drink + ".xlsx")
    print(resultDf.count())



