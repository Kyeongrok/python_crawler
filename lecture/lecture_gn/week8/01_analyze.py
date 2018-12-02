#01_analyze.py
import pandas as pd

df = pd.read_json("./search_result.json")
print(df.count())


# pandas는 data를 dataframe으로 만들어 줍니다.
# dataframe안에 데이터를 넣으면 표처럼 쓸 수 있다.
