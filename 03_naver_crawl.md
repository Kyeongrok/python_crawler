## Naver 메뉴 크롤링
네이버 첫 페이지에 들어가면 나오는 메일, 카페, 블로그 등 메뉴 이름을 뽑아내봅니다.

### ul뽑기
2000줄이 넘는 텍스트 뭉치에서 메뉴를 감싸고 있는 부분인 ul만 뽑아 냅니다.
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})
print(ul)
```

결과
```html
<ul class="an_l">
<li class="an_item">
<a class="an_a mn_mail" data-clk="svc.mail" href="http://mail.naver.com/">
<span class="an_icon"></span><span class="an_txt">메일</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_cafe" data-clk="svc.cafe" href="http://section.cafe.naver.com/">
<span class="an_icon"></span><span class="an_txt">카페</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_blog" data-clk="svc.blog" href="http://section.blog.naver.com/">
<span class="an_icon"></span><span class="an_txt">블로그</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_kin" data-clk="svc.kin" href="http://kin.naver.com/">
<span class="an_icon"></span><span class="an_txt">지식인</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_shopping" data-clk="svc.shopping" href="http://shopping2.naver.com/">
<span class="an_icon"></span><span class="an_txt">쇼핑</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_checkout" data-clk="svc.pay" href="http://pay.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버페이</span>
</a>
</li>
<li class="an_item">
<a class="an_a mn_tvcast" data-clk="svc.tvcast" href="http://tv.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버TV</span>
</a>
</li>
</ul>
```

### li 뽑기
ul에서 각각 item에 해당하는 li를 뽑아봅니다.
li는 list item을 줄여서 표시해 놓은 것입니다.

```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

for li in ul:
    print(li)
```

결과
```html
<li class="an_item">
<a class="an_a mn_mail" data-clk="svc.mail" href="http://mail.naver.com/">
<span class="an_icon"></span><span class="an_txt">메일</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_cafe" data-clk="svc.cafe" href="http://section.cafe.naver.com/">
<span class="an_icon"></span><span class="an_txt">카페</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_blog" data-clk="svc.blog" href="http://section.blog.naver.com/">
<span class="an_icon"></span><span class="an_txt">블로그</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_kin" data-clk="svc.kin" href="http://kin.naver.com/">
<span class="an_icon"></span><span class="an_txt">지식인</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_shopping" data-clk="svc.shopping" href="http://shopping2.naver.com/">
<span class="an_icon"></span><span class="an_txt">쇼핑</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_checkout" data-clk="svc.pay" href="http://pay.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버페이</span>
</a>
</li>


<li class="an_item">
<a class="an_a mn_tvcast" data-clk="svc.tvcast" href="http://tv.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버TV</span>
</a>
</li>

```

### .findAll()로 li만 골라내기
.findAll()을 사용해봅니다.
li가  []리스트 안으로 들어옵니다.

```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li")

print(lis)
```

결과
```text
[<li class="an_item">
<a class="an_a mn_mail" data-clk="svc.mail" href="http://mail.naver.com/">
<span class="an_icon"></span><span class="an_txt">메일</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_cafe" data-clk="svc.cafe" href="http://section.cafe.naver.com/">
<span class="an_icon"></span><span class="an_txt">카페</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_blog" data-clk="svc.blog" href="http://section.blog.naver.com/">
<span class="an_icon"></span><span class="an_txt">블로그</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_kin" data-clk="svc.kin" href="http://kin.naver.com/">
<span class="an_icon"></span><span class="an_txt">지식인</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_shopping" data-clk="svc.shopping" href="http://shopping2.naver.com/">
<span class="an_icon"></span><span class="an_txt">쇼핑</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_checkout" data-clk="svc.pay" href="http://pay.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버페이</span>
</a>
</li>, <li class="an_item">
<a class="an_a mn_tvcast" data-clk="svc.tvcast" href="http://tv.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버TV</span>
</a>
</li>]
```

### li에 들어있는 a뽑기
한단계 더 접근 해봅니다.
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    print(a_tag)
```

```text
<a class="an_a mn_mail" data-clk="svc.mail" href="http://mail.naver.com/">
<span class="an_icon"></span><span class="an_txt">메일</span>
</a>
<a class="an_a mn_cafe" data-clk="svc.cafe" href="http://section.cafe.naver.com/">
<span class="an_icon"></span><span class="an_txt">카페</span>
</a>
··· 중략 ···
<a class="an_a mn_tvcast" data-clk="svc.tvcast" href="http://tv.naver.com/">
<span class="an_icon"></span><span class="an_txt">네이버TV</span>
</a>

```

### a안에 span중 class가 an_txt인 것 뽑아내기
한단계 더 들어가지만 같은 level에 태그가 2개 이상인 경우 class를 사용합니다.

```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span)
```

결과
```text
<span class="an_txt">메일</span>
<span class="an_txt">카페</span>
<span class="an_txt">블로그</span>
<span class="an_txt">지식인</span>
<span class="an_txt">쇼핑</span>
<span class="an_txt">네이버페이</span>
<span class="an_txt">네이버TV</span>

```

### 글자만 뽑아내기
```python
import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"an_l"})

lis = ul.findAll("li")

for li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)
    
```

결과
```text
메일
카페
블로그
지식인
쇼핑
네이버페이
네이버TV
```