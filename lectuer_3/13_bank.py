import requests
from bs4 import BeautifulSoup

def get_bs_obj(url):
    middle = requests.get(url)
    bs_obj = BeautifulSoup(middle.content, "html.parser")
    return bs_obj
def print_rate(bs_obj):
    table = bs_obj.find("table",{"class":"gridHeaderTableDefault"})


url= "http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/startest/BISBndSrtPrcDay.xml&divisionId=MBIS01070010000000&divisionNm=%25EC%259D%25BC%25EC%259E%2590%25EB%25B3%2584&tabIdx=1&w2xHome=/xml/&w2xDocumentRoot="
xml = """<?xml version: "1.0" encoding="utf-8"?>
<message>
  <proframeHeader>
    <pfmAppName>BIS-KOFIABOND</pfmAppName>
    <pfmSvcName>BISBndSrtPrcSrchSO</pfmSvcName>
    <pfmFnName>selectDay2</pfmFnName>
  </proframeHeader>
  <systemHeader></systemHeader>
<BISBndSrtPrcDayDTO><standardDt>20181012</standardDt><reportCompCd>A10000</reportCompCd><applyGbCd>C02</applyGbCd></BISBndSrtPrcDayDTO></message>"""
headers = {'User-Agent': 'Mozilla/5.0'}
result = requests.post(url, headers=headers, data=xml).content
print(result)
