import pandas as pd

df = pd.read_json("./search_result.json")
df = df[df['postdate'].str.contains('2018')]
print(df.count())

# 2018년 데이터만 대상으로 아래 키워드의 포스트 등장 회수를 알고 싶다.

dfgogi = df[df['title'].str.contains("고기집")]
dfhut = df[df['title'].str.contains("횟집")]
dfpython = df[df['title'].str.contains("파이썬")]

print(dfgogi.count())
print(dfhut.count())
print(dfpython.count())

# print(dfpython['postdate'])

# print(df2[['postdate', 'title', 'link']].head(30))

# 강남역 맛집 등으로 검색 했을 때 횟집결과가 많을까요?
# 고기집 결과가 많을 까요?