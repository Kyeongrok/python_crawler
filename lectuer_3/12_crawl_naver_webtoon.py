import urllib.request
import bs4

url="https://comic.naver.com/webtoon/list.nhn?titleId=20853"
html = urllib.request.urlopen(url)

bs_obj=bs4.BeautifulSoup(html,"html.parser")
table = bs_obj.find("table",{"class":"viewList"})
td = table.findAll("td",{"class":"title"})

print(type(td))
print(td)
print(td[0])

for number in range(0, len(td)):
    print(td[number].text)
