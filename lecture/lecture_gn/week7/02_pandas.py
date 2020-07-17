# python pandas
# data분석 툴
# 파이썬 안에서 표 형태의 데이터를 분석할때 씁니다.
# excel like
import pandas as pd

dataframe = pd.read_json("./data_file.json")
print(dataframe['bloggername'])

