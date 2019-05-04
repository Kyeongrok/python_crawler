import pandas as pd
import matplotlib.pyplot as plt

dfcar = pd.read_json("./카네이션.json")
dfchild = pd.read_json("./어린이날.json")
dfchu = pd.read_json("./추석.json")

def getGroupByPrice(df):
    bins = pd.cut(df['price'], [0, 5000,  10000, 20000, 30000, 50000, 120000])
    gb = df.groupby(bins)['price']
    gbagg = gb.agg(['count', 'sum'])


    return gbagg

gbCar = getGroupByPrice(dfcar)
gbChild = getGroupByPrice(dfchild)
gbChu = getGroupByPrice(dfchu)
print(gbCar['count'])

plt.plot(["~5000", "5~10k", "10k~20k", "20k~30k", "30~50k", "50~120k"],
         gbCar['count'], label="carnation")
plt.plot(["~5000", "5~10k", "10k~20k", "20k~30k", "30~50k", "50~120k"],
         gbChild['count'], label="child")
plt.legend()
plt.show()