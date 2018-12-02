import pandas as pd
df = pd.read_json("./search_result.json")

df2 = df[['postdate', 'title', 'bloggername', 'link']]
df2Sorted = df2.sort_values(['postdate'], ascending=[0])
df2SortedAndTop10 = df2Sorted[['postdate', 'title', 'link']].head(10)

for item in df2SortedAndTop10['link']:
    print(item)

# writer = pd.ExcelWriter('top10.xlsx')
# df2SortedAndTop10.to_excel(writer,'top10')
# writer.save()
