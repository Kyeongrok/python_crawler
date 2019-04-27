import pandas as pd
pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./gangnam.json")

def save(dictList, filename):
    writer = pd.ExcelWriter(filename)
    for dict in dictList:
        dict['df'].to_excel(writer, dict['sheetName'])
    writer.save()

dfSorted = df.sort_values(['postdate'], ascending=[False])
dfFilter = dfSorted[dfSorted['title'].str.contains("스테이크")]
list = [
    {"sheetName":"origin", "df":df},
    {"sheetName":"top10", "df":dfSorted.head(10)},
    {"sheetName":"bottom10", "df":dfSorted.tail(10)},
    {"sheetName":"스테이크", "df":dfFilter},
    {"sheetName":"sorted", "df":dfSorted}
]
save(list, "sorted.xlsx")
