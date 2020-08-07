from libs.crawler import crawl
from bs4 import BeautifulSoup
import requests, re

'''
1.매출액-시총 >=0
2.(영업이익*10)배 - 시총 >=0
3.bps >=0   --- 0
4.bps-현재가 >=0   --- 0
5.(유보율:부채비율 = 5:1)<= 20%
6.이익잉여금 >=0
7.이익잉여금-시총 >=0
8.영업이익증가율 >=0
9.per <=10
10.roe >=0
11.roa >=0
12.pbr <=1
13.eps >=0
'''

url = 'https://finance.naver.com/item/main.nhn?code=005930'
# string = crawl(url)
# open('005930.html', 'w+').write(requests.get(url).text)
string = open('target_site_file/005930.html', encoding='utf-8').read()


replace_space = lambda x: re.sub("(\n|\t|\\xa0|,)", "", x)


def parse(string):
    bsobj = BeautifulSoup(string, 'html.parser')
    aside = bsobj.find('div', {'id':'aside'})
    tab_con1 = aside.find('div', {'id':'tab_con1'})


    pbr = 0
    bps = 0
    price_today = 0
    sales = 0
    net_income = 0
    market_cap = 0

    operating_profit = 0

    # 최근 연간 매출
    cop_analysis = bsobj.find('div', {'class':'section cop_analysis'})
    tr_t_line = cop_analysis.find('thead').find_all('tr')[1].find_all('th')[2].text
    last_year = replace_space(tr_t_line)

    tbody_trs = cop_analysis.find('tbody').find_all('tr')
    tbody_first_tr_tds = tbody_trs[0].find_all('td')
    tbody_second_tr_tds = tbody_trs[1].find_all('td')
    tbody_third_tr_tds = tbody_trs[2].find_all('td')
    sales = float(replace_space(tbody_first_tr_tds[2].text))

    # operating profit 영업이익
    operating_profit = float(replace_space(tbody_second_tr_tds[2].text))

    # 당기순이익
    net_income = float(replace_space(tbody_third_tr_tds[2].text))


    # 시가총액
    div_first_tbody_trs = tab_con1.find('div', {'class':'first'}).find_all('tr')
    market_cap = re.sub('(\t|\n)','',div_first_tbody_trs[0].find('td').text)
    print(market_cap)



    # 현재가sdf
    try:
        price_today = bsobj.find('p', {'class':'no_today'}).find('span', {'class':'blind'}).text.replace(',','')
        price_today = float(price_today)
    except Exception as e:
        print(e)

    try:
        per_table = tab_con1.find('table', {'class': 'per_table'})
        per_table_trs = per_table.find_all('tr')
        ems = per_table_trs[2].find_all('em')
        pbr = float(ems[0].text)
        bps = float(ems[1].text.replace(',', ''))
    except Exception as e:
        print(e)

    # 전년도 매출
    return {'price_today':price_today, 'bps':bps, 'pbr':pbr, 'bps_minus_today_price':bps - price_today,
            'sales{}'.format(last_year):sales*pow(10, 8), 'operating_profit{}'.format(last_year):
    operating_profit * pow(10, 8), 'net_income':net_income * pow(10, 8)}

print(parse(string))