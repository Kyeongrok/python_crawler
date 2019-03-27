import pandas as pd

location = "/Users/kyeongrok/Desktop/"
df = pd.read_json(location + "result_year_authors_nation.json")

writer = pd.ExcelWriter(location +'output.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()