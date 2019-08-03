import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', 100)

# df = 표
df = pd.read_json("./coffee.json")

def printInfos(keyword):
    dfFiltered = df[df['name'].str.contains(keyword)]
    dfFiltered2 = dfFiltered[(dfFiltered['price'] >= 10000) &(dfFiltered['price'] < 20000)]
    dfSorted = dfFiltered2.sort_values(['price'], ascending=False)
    print("count:", len(dfSorted['price']))
    print("max:", dfSorted.head(1)['price'])
    print("min:", dfSorted.tail(1)['price'])
    print("----------------------------")

# 맥심이라는 키워드가 들어있고 가격대가 10000 <= x < 20000
# 1.위 조건의 데이터는 몇건인지?
# 2.가장 비싼 물건의 이름은?

printInfos("맥심")
printInfos("네스카페")
printInfos("네스프레소")


