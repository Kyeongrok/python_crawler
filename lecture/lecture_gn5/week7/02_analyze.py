import pandas as pd
import matplotlib.pylab as plt
import numpy as np
pd.set_option('display.max_colwidth', -1)

def analyzeJson(fileName):
    df = pd.read_json(fileName)

    print(df.count())

    dfSorted = df.sort_values(by=['price'], ascending=False)

    print(dfSorted.head(5))
    print(dfSorted.tail(5))

    # 가격 10000 <= price, 20000 >= price
    df10to20 = dfSorted[dfSorted['price'] >= 10000]
    print(df10to20.tail(5))
    print(df10to20.head(5))

    bins = pd.cut(dfSorted['price'], [0, 5000,  10000, 20000, 30000, 50000, 120000])
    gb = dfSorted.groupby(bins)['price'].agg(['count', 'sum'])
    print(gb)

#analyzeJson("./카네이션.json")
analyzeJson("./어린이날.json")

