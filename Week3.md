## BeautifulSoup
BeautifulSoup(뷰티풀솝)은 데이터를 추출하는데 필요한 기능이 들어있는 라이브러리 입니다.
* 반도체공장(모래) = BeautifulSoup(html)
   

###  BeautifulSoup 사용법
```python
import bs4
str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(str, "html.parser")

print(bsObj)
```

## 크롤링이란?
인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
* 라이브러리 : urlopen

## 파싱이란?
크롤링한 데이터에서 값을 뽑아내는 것
* 라이브러리:bs4 BeautifulSoup 뷰티풀솝
