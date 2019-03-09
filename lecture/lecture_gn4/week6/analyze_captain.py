import pandas as pd

df = pd.read_json("./captin_marble.json")
print(df.count())

def save(list, filename):
    writer = pd.ExcelWriter(filename)

    for dict in list:
        dict['df'].to_excel(writer, dict['sheetName'])
    writer.save()

save([{"df":df, "sheetName":"sheet1"}], "captain_marble.xlsx")

