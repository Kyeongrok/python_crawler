import pandas as pd

df = pd.read_json("./coupangResults.json")

writer = pd.ExcelWriter('outputCoupang.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()
