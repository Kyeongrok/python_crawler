import pandas as pd
from libs.excelSaver import save
from libs.singleExcelSaver import save as sin_save

df = pd.read_json('hello.json')

print(df.shape)
print(df.count())

d_so = df.sort_values('count', ascending=False)

sin_save(d_so, 'hello.xlsx')