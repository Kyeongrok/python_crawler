import urllib.request
import bs4

url = "http://ko.pokemon.wikia.com/wiki/%EC%9D%B4%EC%83%81%ED%95%B4%EC%94%A8_(%ED%8F%AC%EC%BC%93%EB%AA%AC)/1%EC%84%B8%EB%8C%80_%EA%B8%B0%EC%88%A0"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")
print(bs_obj)
