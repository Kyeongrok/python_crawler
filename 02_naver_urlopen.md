## 네이버 첫 페이지 불러오기
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

print(bs_obj)
```
1.urllib.request를 import한다.
2.bs4를 import한다.
3.bs_obj변수에 BeautifulSoup한 결과를 저장한다.
4.출력한다.
