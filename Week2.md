## 목표
naver의 메뉴를 크롤링 한다

## 기본 개념과 용어들
* url : 인터넷 주소
* http : 인터넷 주소 앞에 붙는 것 protocol
* html : 인터넷에서 문서를 보여줄때 쓰는 표현식들
    * hyper text markup language(HTML)
    * 하이퍼텍스트 마크업 랭기지
* server : 페이지를 서빙해주는 곳 (naver, google)

## 라이브러리(library)
    * 도서관이라는 뜻
    * 책이 여러권 있는 곳이 도서관인데
    * 파일이 여러개 있는걸 묶어놓은 것을 라이브러리라고 함
    * 라이브러리는 import를 해서 사용 합니다.
    * 처음 import하면 빨간줄이 나옵니다.
    * 설치를 해주어야 합니다.

## 라이브러리 설치 하는 방법
    * Pettings(Preferance) -> interpreter검색
    * +를 누르고 설치하고 싶은 라이브러리 검색 ex)urlopen

## 크롤링이란?
    * 인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
    * 라이브러리 : urlopen

## 파싱이란?
    * 크롤링한 데이터에서 값을 뽑아내는 것
    * 라이브러리:bs4 BeautifulSoup 뷰티풀솝

## urllib
* 크롤링 하는 라이브러리
* 모래를 퍼온다.

## BeautifulSoup
    * 파싱을 하는 라이브러리
    * 반도체공장(모래) = BeautifulSoup(html)
    
### CSS
* Cascading Style Sheet
* css selector
* 페이지 내에 데이터(한 단어)가 있는 곳의 주소
* html tag

## 트리구조
<pre>
여행가는 책
책시작
	1장 비행기 타는 법
		1절 한국에서 가능법
		2절 외국에서 오는법
	2장 숙소로 이동 하는 법
책끝 맺음말
</pre>

```html
<html>
	<div>
		<ul>
			<li>
				<a>
					<span>
```

## html 태그
```html
<html>, <div>, <ul>, <li>, <a>, <span> 등이 있다.
```

## url알아내는 법
* 크롬 개발자 도구를 사용 한다.
* 메뉴 - 도구 더보기 - 개발자 도구
* Network 탭으로 이동한다.
* XHR선택한다.
* 새로고침 또는 page이동을 한다.
* Headers탭을 누른다.
* Request URL을 확인 한다.
 
 ## []에 대해서
 * [] = list
 * []에는 값이 0개 한개 또는 여러개 들어갈 수 있습니다.
 * 각 값들은 ,로 구분 합니다.
 * ex) [1, 2, 3], [<li></li>,<li></li>]
 * 이렇게 생긴걸 list라는 자료구조 라고 합니다.

## tree, list 자료구조
* tree는 나뭇가지 처럼 뻗어 나가는 것
    * ex) 책의 장, 절
    * 조직도
* list는 순서대로 나열
    * ex) 식당 기다리는 순서
    * 학생 목록(출석부)

## find 사용법
* .find("<찾고싶은tag>")
* ex) item.find("a")

## .find(), findAll()
* .find()는 한개인 것을 찾을 때 씁니다
* .findAll()은 여러개인 것을 찾을 때 씁니다.
 
## JSON
    * javascript object notation(JSON)
    * 자바스크립트 오브젝트 표현법
    * tree구조
    * key, value

```
    {}한개, []여러개
    atag, atags
    {list:[
            {name:"kyeongrok", age:"32"},
            {name:"bomi", age:"25"},
            {name:"cl", age:"27"}
        ]
    }
    
    {list:[]}
    
    [
        {"href":"www.naver.com", name:"naver"},
        {"href":"www.google.com", name:"google"},
        {},
        {}
    ]
```

## json 편하게 보는 site
* json tree
* http://jsonviewer.stack.hu/

## 실습
1. http request하기
2. url 알아내서 a tag출력하기
3. 아래 data json으로 바꾸기
```
    이름	가격	위치
    cozy 모임공간	2500	강남역 3번출구
    스터디 플래닛	3000	역삼역과 강남역 근처
    에이지 스토리	2000	서울대입구역
    스타벅스	5000	많음
```
