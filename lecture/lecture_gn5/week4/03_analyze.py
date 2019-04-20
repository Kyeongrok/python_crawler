import pandas as pd
from libs.singleExcelSaver import save

df = pd.read_json("./candy.json")
print(df.count())

save(df, "./candy.xlsx")