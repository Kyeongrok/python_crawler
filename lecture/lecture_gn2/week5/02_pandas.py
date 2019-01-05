import pandas as pd

df = pd.read_json("./results.json")

writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
