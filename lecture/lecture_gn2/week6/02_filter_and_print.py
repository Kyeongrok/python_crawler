import pandas as pd
pd.set_option('display.max_colwidth', -1)
# pandas로 데이터 불러오기
df = pd.read_json("./naverKeywordResult.json")

for bloggername in df.head(100)['bloggername']:
    dfResult = df[df['bloggername'] == bloggername]
    print(bloggername, len(dfResult))

dfTop1 = df[df['bloggername'] == "책과 음식과 영화이야기"]
for item in dfTop1['link']:
    print(item.replace("amp;", ""))
