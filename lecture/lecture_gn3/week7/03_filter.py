import pandas as pd
from libs.excelSaver import save
pd.set_option('display.max_colwidth', -1)
df = pd.read_json("./195297.json")

brands = ["킨더", "페레로로쉐", "벨지안", "엠엔앰", "누텔라", "마켓오", "롯데"]

for brandName in brands[:1]:
    dfFiltered = df[df['name'].str.contains(brandName)]
    dfSortedDesc = dfFiltered.sort_values(['price'], ascending=[0])
    dfSortedAsc = dfFiltered.sort_values(['price'], ascending=[1])
    dfPriceUpper = dfSortedDesc[dfSortedDesc['price'] >= 10000]
    dictList = [
        {'df':dfSortedDesc.head(10), 'sheetName': 'top10'},
        {'df':dfSortedAsc.head(10), 'sheetName': 'tail10'},
        {'df':dfPriceUpper, 'sheetName': 'upper10000'},
    ]
    save(dictList, brandName + ".xlsx")
    # price top10
    # price 뒤에서 top10





