import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', 100)

# df = 표
df = pd.read_json("./coffee.json")
def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()

dfSorted = df.sort_values(['price'], ascending=False)

save(dfSorted, "./coffee.xlsx")
