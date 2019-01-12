import pandas as pd

# pandas로 데이터 불러오기
df = pd.read_json("./naverKeywordResult.json")

# 잘 불러왔느지 확인하기
print(df.count())

# 데이터가 어떻게 생겼는지 알아보기

# column명, 필드(field)명, 열제목

# 블로거 이름을 가지고 필터링 하기
# 블로거 이름이 기준

# top5 블로거가 검색결과 1000개중에 글을 몇개나 썼을까요?
# 가장 많이 글을 쓴 블로거는 누구일까요?

print(df.head(5)['bloggername'])

dfResult = df[df['bloggername'] == "명랑 뮬란의 오늘 뭐먹지?"]


