#01_analyze.py
#openpyxl
import pandas as pd

df = pd.read_json("./search_result.json")
print(df.count())

writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()