import pandas as pd

df = pd.read_excel("./jongmok.xlsx")
print(df['code'])

for item in df['code']:
    print(item.replace("'", ""))
