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