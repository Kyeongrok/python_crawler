import pandas as pd
df = pd.read_json("./search_result.json")

df2 = df[['bloggername', 'link', 'title']]
df3 = df[df['bloggername'] == '허니드롭']

print(df3['title'])
for link in df3['link']:
    print(link)
