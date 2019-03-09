import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./mandoo.json")
print(df.count())

#https://krksap.tistory.com/1468


# 제일 비싼거 10개, 제일 싼거 10개
dfSorted = df.sort_values(['price'])

print(dfSorted[['name', 'price']].head(10))
print(dfSorted[['name', 'price']].tail(10))

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1')
    writer.save()

dfSorted = dfSorted[['name', 'price','link']]
save(dfSorted, "./mandoo.xlsx")

