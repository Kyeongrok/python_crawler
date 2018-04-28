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

## 라이브러리(library)
라이브러리(library)는 도서관이라는 뜻입니다. 책이 여러권 있는 곳이 도서관인데 여러가지 기능들이 있는 코드 묶음을 라이브러리라고 합니다.
* 많이 사용하는 기능들을 다른 사람 또는 회사가 만들어서 올려놓은 것입니다.
* 라이브러리는 import를 해서 사용 합니다.
* 내장 라이브러리와 외장 라이브러리가 있습니다.
* 내장 라이브러리는 import해서 사용하고 외장 라이브러리는 설치한 후 import해서 사용합니다.

## 라이브러리 설치 하는 방법
* Pettings(Preferance) -> interpreter검색
* +를 누르고 설치하고 싶은 라이브러리 검색 ex)bs4, numpy 등


## 네이버 첫 페이지 받아오기
```python
from urllib.request import urlopen

url = "https://www.naver.com/"
html = urlopen(url)

print(html.read())
```
