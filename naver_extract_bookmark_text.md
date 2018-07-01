## Naver 첫페이지 불러오기
```python
import urllib.request

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

print(html.read())
```

## bs4적용하기
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

print(bs_obj)
```

## div태그 뽑아내기
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("div", {"class":"area_links"})
print(top_right)
```

