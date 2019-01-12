import pandas as pd
pd.set_option('display.max_colwidth', -1)
# pandas로 데이터 불러오기
df = pd.read_json("./naverKeywordResult.json")
# 날짜 string형태 '20190112', '20191012'

print(df.columns)
# 20180102 -> %Y%m%d" 날짜형식
# 2018-01-02 -> %Y-%m-%d"
# 2018.01.02 -> %Y.%m.%d"
# 2018년01월02일 -> %Y년%m월%d일"
# 2018년 01월 02일 -> %Y년 %m월 %d일"

df['postdate'] = pd.to_datetime(df['postdate'], format="%Y%m%d")
df = df[df['postdate'] >= '2018-01-01']
print("upper 2017:", df.count())
df = df.head(50)


# 1000개 중에서 2018년 1월에 올라온 글은 몇개일까요?
df2018Jan = df[(df['postdate'] >= "2018-01-01") & (df['postdate'] <= "2018-01-31") ]
df2018Feb = df[(df['postdate'] >= "2018-02-01") & (df['postdate'] <= "2018-02-28") ]
df2018Mar = df[(df['postdate'] >= "2018-03-01") & (df['postdate'] <= "2018-03-31") ]
print(df2018Jan.count())
print(df2018Feb.count())
print(df2018Mar.count())

for item in df2018Jan['link']:
    print(item.replace("amp;", ""))

print(df['postdate'].min())
print(df['postdate'].max())
