# 생수 라는 키워드 검색 결과를 27페이지까지
# 수집하고 브랜드별 점유율을 파이차트로
# 그려보세요.
# str.contains(브랜드명)
import pandas as pd

df = pd.read_json("./생수.json")

brands = ["삼다수", "아이시스", "스파클", "에비앙", "평창수"]


def getCount(df, brandName):
    # name에 특정 브랜드명이 있는 항목을 필터링
    dfFiltered = df[df['name'].str.contains(brandName)]
    return len(dfFiltered['name'])

cnts = []
for brand in brands:
    cnt = getCount(df, brand)
    cnts.append(cnt)
print(cnts)
total = len(df['name'])
print(total)
print(sum(cnts))

shares = [cnt / total * 100 for cnt in cnts]

# for cnt in cnts:
#     result = cnt / total * 100
#     shares.append(result)

brandsKor = ["samda", "isis", "spa", "ebi", "pye"]

from matplotlib import pyplot as plt
# plt.pie(shares, labels=brandsKor, autopct='%1.1f%%')
plt.bar(brandsKor, cnts)
plt.show()
