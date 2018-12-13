import pandas as pd

location = "/Users/kyeongrok/Desktop/"
df = pd.read_json(location+"result3.json")

authors = df['authors']
institutions = df['institutions']

for institution in institutions:
    print(len(institution))



