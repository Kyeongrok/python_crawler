#android6265 pw:1q2w3e4r
import pandas as pd

#dataframe
df = pd.read_json("./195297.json")
print(df.count())

print(df['price'])
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()