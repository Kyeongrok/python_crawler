import pandas as pd

location = "/Users/kyeongrok/Desktop/"
urlPrefix = "https://www.ncbi.nlm.nih.gov/pubmed/"
df = pd.read_json(location+"result1000.json")

def getNations(instutions):
    nations = []
    for institution in instutions:
        arr = institution.split(", ")
        nations.append(arr[len(arr) - 1])
    return nations

df['nation'] = df.apply(lambda row: getNations(row['institutions']), axis=1)

# for index, row in df.iterrows():
#     print(urlPrefix + str(row['id']), len(row['institutions']), row['institutions'])
#     row['nation'] = "hh"

print(df['nation'])


