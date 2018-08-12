import urllib.request
import bs4

url = "https://finance.naver.com/world/sise.nhn?symbol=DJI@DJI&fdtc=0"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(bs_obj)

