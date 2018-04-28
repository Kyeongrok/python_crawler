# 가장 먼저 해야 하는 것은?
'''
    명령어를 치고
    url을 가지고 오고
    data가 오는지 확인 해볼 것

    제목
    제목이 들어 있는 곳을 찾는다.

    ul을 찾음 - 리스트 찾기
    for문 이용해서 li하나씩 뽑아오기

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://m.pann.nate.com/talk/c20028"
html = urlopen(url)

bsObj = BeautifulSoup(html, "html.parser")

ul = bsObj.find("ul", {"class":"list rank-list"})

for li in ul:
    result = li.find("a")
    # 제목뽑기
    print(result)

