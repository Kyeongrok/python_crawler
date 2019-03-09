import pandas as pd

df = pd.read_json("./result.json")
print(df.count())

def save(list, filename):
    writer = pd.ExcelWriter(filename)

    for dict in list:
        dict['df'].to_excel(writer, dict['sheetName'])
    writer.save()

brands = ["아이시스", "몽베스트", "스파클", "풀무원", "에비앙", "삼다수", "동원", "평창수"]

for brand in brands:
    dfFiltered = df[df['name'].str.contains(brand)]
    dfSorted = df.sort_values(['price'])
    dfTop5 = dfFiltered.head(5)
    dfTail5 = dfFiltered.tail(5)
    list = [
        {"df":dfSorted, "sheetName":"sorted"},
        {"df":dfTop5, "sheetName":"top5"},
        {"df":dfTail5, "sheetName":"tail5"}
    ]
    save(list, brand + ".xlsx")
    nowCount = len(dfFiltered['name'])
    print(brand, nowCount, nowCount/len(df['name']) * 100)

