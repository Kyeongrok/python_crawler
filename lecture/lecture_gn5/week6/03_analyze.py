import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./gangnam.json")
print(df.count())

dfSorted = df.sort_values(['postdate'], ascending=[False])
def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()


# 가장 많이 등장한 블로거

# 스테이크, 파스타, 평양냉면, 만두, 피자, 아이스크림, 팥빙수
def analyzeByFood(fromDate, toDate, df):
    foods = ["스테이크", "고기", "삼겹살", "파스타", "평양냉면", "만두", "피자", "아이스크림", "팥빙수"]
    for food in foods:
        dfFiltered = df[df['title'].str.contains(food)]
        print(food, fromDate, toDate, len(dfFiltered['title']))
        # save(dfFiltered, "{}.xlsx".format(food))

# 월별로 음식 선호도
for month in range(1, 12):
    fromDate = 20180101 + (month - 1) * 100
    toDate = fromDate + 100
    dfFiltered2019jan = dfSorted[(dfSorted['postdate']>=fromDate) & (df['postdate']<toDate)]
    # print(len(dfFiltered2019jan['title']))
    analyzeByFood(fromDate, toDate, dfFiltered2019jan)
    # save(dfFiltered2019jan, "{}-{}.xlsx".format(fromDate, toDate))
