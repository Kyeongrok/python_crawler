import pandas as pd
import json

from libs.excelSaver import save

df = pd.read_json("./result.json")
dfDrinkMilk = df[df['name'].str.contains("우유")]

competitors = ["매일", "서울", "남양", "파스퇴르", "연세"]

def getReportTable(competitors):
    reportTable = []
    for competitor in competitors:
        result = df[df['name'].str.contains(competitor)]
        # 합계 평균 표준편차
        sum = result['price'].sum()
        mean = result['price'].mean()
        std = result['price'].std()
        max = result['price'].max()
        min = result['price'].min()
        count = result['price'].min()
        row = {
            "competitor":competitor,
            "sum": sum,
            "mean": mean,
            "max": max,
            "min": min,
            "count": count
        }


        reportTable.append(row)
    return reportTable

reportTable = getReportTable(competitors)

dfReportTable = pd.DataFrame(reportTable)

save(dfReportTable, "week3Report.xlsx")


# json으로 만들고
# excel file로 저장 해보세요


