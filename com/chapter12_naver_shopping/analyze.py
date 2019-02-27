import pandas as pd

df = pd.read_json("./tumbler.json")

print(df.count())

writer = pd.ExcelWriter("./tumbler.xlsx")
df.to_excel(writer, "sheet1")
#openpyxl
