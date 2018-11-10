import requests
from bs4 import BeautifulSoup

url = "http://bigdata-trader.com/itemcodehelp.jsp"
result = requests.get(url)
bsObj = BeautifulSoup(result.content, "html.parser")

trs = bsObj.find("table").findAll("tr")

codes = [tr.find("a").text + "\n" for tr in trs]

file = open("./codes.txt", "w+")
file.writelines(codes)
