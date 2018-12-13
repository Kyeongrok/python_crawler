import pandas as pd

location = "/Users/kyeongrok/Desktop/"
df = pd.read_json(location+"result3.json")

authors = df['authors']
institutions = df['institutions']

for institution in institutions:
    print(len(institution))

df1000 = df.head(1000)
print(df1000.count())

df1000.to_json(location + "result1000.json")
