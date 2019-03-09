import pandas as pd
from libs.excelSaver import save

pd.set_option('display.max_colwidth', -1)
df = pd.read_json("./195297.json")
dicts = [
    {'df':df, 'sheetName': 'total'},
]
save(dicts, "초콜렛.xlsx")

print(df.count())
