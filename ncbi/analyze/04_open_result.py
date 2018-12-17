import pandas as pd

df = pd.read_json("/Users/mattheu/Desktop/result_year_nation.json")
print(df.count())

print(df['authors'])

for author in df['authors']:
    print(author)