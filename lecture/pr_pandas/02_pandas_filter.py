import pandas as pd

pd.set_option('display.max_colwidth', -1)

df = pd.read_json("./naverKeywordResult.json")
print(df.count())

bloggerName = "명랑 뮬란의 오늘 뭐먹지?"
dfFiltered = df[df['bloggername'] == "명랑 뮬란의 오늘 뭐먹지?"]
print(dfFiltered.count())

print(dfFiltered['bloggername'])
print(dfFiltered['link'][1].replace("amp;", ""))
