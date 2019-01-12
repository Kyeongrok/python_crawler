import pandas as pd

df = pd.read_json("./naverKeywordResult.json")
print(df.count())

# 상위 10개 블로거 이름
dfTop5 = df.head(5)
print(dfTop5['bloggername'])
