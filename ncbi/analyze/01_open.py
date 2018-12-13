import pandas as pd
import re
location = "/Users/kyeongrok/Desktop/"
df = pd.read_json(location+"result2.json")

pattern = re.compile("[0-9]{4}")
df['year'] = df.apply( lambda row: pattern.findall(row['journal'])[0], axis=1)

df.to_json(location + "result3.json")

