from libs.crawler import crawl
from bs4 import BeautifulSoup
import requests

url = 'https://finance.naver.com/item/main.nhn?code=005930'
# string = crawl(url)
# open('samsung.html', 'w+').write(requests.get(url).text)
string = open('samsung.html', encoding='utf-8').read()
bsobj = BeautifulSoup(string, 'html.parser')

aside = bsobj.find('div', {'id':'aside'})
tab_con1 = aside.find('div', {'id':'tab_con1'})
per_table = tab_con1.find('table', {'class':'per_table'})
trs = per_table.find_all('tr')
bps = ''

for tr in trs:
    print(tr)
