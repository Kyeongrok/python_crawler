import requests
from bs4 import BeautifulSoup

url = "http://search.itooza.com/index.htm?seName=005930"

def company(code):
    print("company code:{}".format(code))
    url = "http://search.itooza.com/index.htm?seName=" + code
    result = requests.get(url)
    soup = BeautifulSoup(result.content.decode("euc-kr", "replace"), "html.parser")
    table = soup.find("div", {"id": "indexTable2"})
    tds = table.findAll("td")
    for td in tds[85:95]:
        print(td.text)

companies = ["005930", "000660"]

for company_code in companies:
    company(company_code)