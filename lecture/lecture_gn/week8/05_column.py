import pandas as pd
df = pd.read_json("./search_result.json")

dfLink = df['link']
print(dfLink)

writer = pd.ExcelWriter('links.xlsx')
dfLink.to_excel(writer,'link')
writer.save()
