import pandas as pd
import json
from libs.excelSaver import save
from libs.singleExcelSaver import save as sin_save

df = pd.read_json('hello3.json')
df['type_count'] = df['service_types'].apply(lambda x: len(x))
# print(df['service_types'])
print(df.shape)

df_fil = df[df['title'].str.contains('마사회')]
print(df_fil)
# print(df_fil.head(1)['service_types'])


# sin_save(df_filtered, '20200622_openapi_가격.xlsx')

# print(df.shape)
# print(df.count())
#
# d_so = df.sort_values('count', ascending=False)
#
# sin_save(d_so, 'hello2.xlsx')