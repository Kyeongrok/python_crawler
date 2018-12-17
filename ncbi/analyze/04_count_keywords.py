import pandas as pd

df = pd.read_json("/Users/kyeongrok/Desktop/result3.json")
print(df.count())

print(df['authors'])

count = 0
for author in df['year']:
    print(author)
print(count)