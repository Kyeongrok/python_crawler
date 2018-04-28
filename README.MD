## Python 기초
[1주차](https://github.com/Kyeongrok/python_example)

* 파이썬 프로젝트 만들기
* function, parameter, return


## 데이터 수집 기초
[2주차 내용](./Week2.md)

* 크롤링이란, 파싱이란?
* 라이브러리란? 라이브러리 설치하기
* http, html, css

## Certificate 에러 날 때
Python이 설치된 경로에 들어가 Install Certificates.command 한다

## 파이썬 라이브러리 설치하기
* 도서관이라는 뜻
* 책이 여러권 있는 곳이 도서관인데
* 파일이 여러개 있는걸 묶어놓은 것을 라이브러리라고 함
* 라이브러리는 import를 해서 사용 합니다.
* 처음 import하면 빨간줄이 나옵니다.
* 설치를 해주어야 합니다.

## 라이브러리 설치 하는 방법
* Pettings(Preferance) -> interpreter검색
* +를 누르고 설치하고 싶은 라이브러리 검색 ex)urllib, bs4


## 네이버 첫 페이지 받아오기
```python
from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)

print(html.read())
```
