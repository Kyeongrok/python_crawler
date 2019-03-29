import pandas as pd

# df = pd.read_json("./bible.json")
# print(df.count())

import json

file = open("./bible.json")
jsonObj = json.loads(file.read)

print(jsonObj)