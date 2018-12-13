import pandas as pd
import re

location = "/Users/kyeongrok/Desktop/"
urlPrefix = "https://www.ncbi.nlm.nih.gov/pubmed/"
df = pd.read_json(location+"result3.json")

regex = re.compile(r".\.*")

def getNations(instutions):
    nations = []
    for institution in instutions:
        arr = institution.split(", ")
        nation = arr[len(arr) - 1]

        # China를 포함하고 있으면 China
        if( nation.find("China") >= 0):
            nation = "China"

        if( nation.find("U.S.A") >= 0):
            nation = "USA"

        if( nation.find("U.K") >= 0):
            nation = "UK"

        nation = re.sub("\..*", "", nation)
        nations.append(nation)
    print(nations)
    return nations

df['nation'] = df.apply(lambda row: getNations(row['institutions']), axis=1)


df.to_json(location + "result4.json")
