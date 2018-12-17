import pandas as pd

df = pd.read_json("/Users/mattheu/Desktop/result_year_nation.json")
print(df.count())

print(df['authors'])

count = 0
for author in df['keywords']:
    if(len(author) ==0):
        count = count + 1

print(count)