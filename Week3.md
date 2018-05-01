## BeautifulSoup
BeautifulSoup(뷰티풀솝)은 데이터를 추출하는데 필요한 기능이 들어있는 라이브러리 입니다.
* 반도체공장(모래) = BeautifulSoup(html)
   

###  BeautifulSoup 사용법
```python
import bs4
html_str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bsObj))
print(bsObj)
print(bsObj.find("div"))
```

### 크롤링이란?
인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
* 라이브러리 : urlopen

### 파싱이란?
크롤링한 데이터에서 값을 뽑아내는 것
* 라이브러리:bs4 BeautifulSoup 뷰티풀솝

### ul태그 뽑아내기
위 소스코드는 <div>태그를 뽑아내는 예제였습니다. 이 예제는 ul태그를 뽑아내는 예제 입니다.
```python
import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bsObj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bsObj.find("ul")
print(ul)

```

### 데이터 받아서 파싱하기
네이버에서 맨 오른쪽 위에 있는 '네이버를 시작페이지로'이 글자를 파싱 하는 코드입니다.
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bsObj = bs4.BeautifulSoup(html, "html.parser")

# print(html.read())
# print(bsObj)

top_right = bsObj.find("div", {"class":"area_links"})
first_a = top_right.find("a")
print(first_a.text)
```

