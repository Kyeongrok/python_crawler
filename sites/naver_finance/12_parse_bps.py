from libs.crawler import crawl
from bs4 import BeautifulSoup
import requests

'''
매출액-시총 >=0
(영업이익*10)배 - 시총 >=0
bps >=0
bps-현재가 >=0
(유보율:부채비율 = 5:1)<= 20%
이익잉여금 >=0
이익잉여금-시총 >=0
영업이익증가율 >=0
per <=10
roe >=0
roa >=0
pbr <=1
eps >=0
'''

url = 'https://finance.naver.com/item/main.nhn?code=005930'
# string = crawl(url)
# open('samsung.html', 'w+').write(requests.get(url).text)
string = open('samsung.html', encoding='utf-8').read()

def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')

    aside = bsobj.find('div', {'id':'aside'})
    tab_con1 = aside.find('div', {'id':'tab_con1'})

    # 시총 들어있는 table
    div_first_tbody_trs = tab_con1.find('div', {'class':'first'})

    per_table = tab_con1.find('table', {'class':'per_table'})
    trs = per_table.find_all('tr')
    pbr = 0
    bps = 0

    try:
        ems = trs[2].find_all('em')
        pbr = float(ems[0].text)
        bps = float(ems[1].text.replace(',', ''))
    except Exception as e:
        print(e)

    print(bps, pbr)

parse(string)