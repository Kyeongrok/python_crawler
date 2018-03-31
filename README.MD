## 기본 개념과 용어들
    * url : 인터넷 주소
    * http : 인터넷 주소 앞에 붙는 것 protocol
    * html : 인터넷에서 문서를 보여줄때 쓰는 표현식들
    * server : 페이지를 서빙해주는 곳 (naver, google)

## 크롤링이란?
    * 인터넷 주소로 서버에 데이터를 요청해서 받아오는 것(콘솔에 출력하는 것)
    * 라이브러리 : urlopen

## 파싱이란?
    * 크롤링한 데이터에서 값을 뽑아내는 것
    * 라이브러리:bs4 BeautifulSoup 뷰티풀솝

css
css selector
	페이지 내에 데이터(한 단어)가 있는 곳의 주소
html tag

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

## Beautiful Soup이란?
    * html또는 json형태의 데이터를 트리 구조로 접근 할 수 있게 해주는 라이브러리
    * 파싱을 할 때 사용 합니다. 
 
## JSON
    * hyper text markup language(HTML)
    * 하이퍼텍스트 마크업 랭기지
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