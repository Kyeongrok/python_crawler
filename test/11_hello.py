# crawl
from datetime import datetime
import pandas as pd

print(datetime.now())
print(datetime.now().weekday())


import requests
import json

def call_api(prd_cd, date, key, limit=10):
# 공공데이터 API Call (농수산물 도매시장 경락가격 data)
    url=f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    #parameter 서버로 넘겨주는 정보
    print(url)

    # 데이터불러오기
    r= requests.get(url).content#json파일에 접근

    jo = json.loads(r)
    # item = jo['response']['body']['items']#['item']
    return jo['response']

def save(item, date, prd_cd):
    # 1개 파일 저장
    if item != "":  # item이 널이 아닐때(공휴일, 휴일 등 data가 없음)
        # filename결정
        file_name = f'res_js{date}_{prd_cd}.json'

        # 파일 저장
        with open(file_name, 'w+') as f:
            f.write(json.dumps(item))
            # print(file_name, 'save success')#로그 기록 찍기`


key = 'CTFUEzKcx7CIIBqAvwD%2BJ9MObIpZoglK5TtrmnaBqeaiaFS%2FDlPS2Bt%2Fq52xl%2B33kK8hAHvCMK1b7Mu77hN17w%3D%3D'
date = '20210104'
prd_cd = "1202"
r = call_api(prd_cd, date, key)

rct3 = pd.date_range(start='20200101', end='20200315')
dt_list = rct3.strftime("%Y%m%d").to_list()
print(dt_list)
limit = int(r['body']['totalCnt'])