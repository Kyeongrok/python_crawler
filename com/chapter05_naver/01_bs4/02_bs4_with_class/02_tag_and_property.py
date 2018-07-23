import bs4

html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul> 
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# tag   태그  <ul></ul> <li></li> <div></div> <a></a> => <a />
# property  속성 class, id, href, title, src
# property value 속성값 class="greet"에서 greet이 속성값
# <a href="www.google.com">구글</a> 태그와 속성값은 각각 무엇일까요?
# tag? a, property(속성) href, 속성값 of href : www.google.com
# html <html></html>

# ok no sure
ul_reply = bs_obj.find("ul", {"class":"reply"})
lis = ul_reply.findAll("li")

for li in lis:
    print(li.text)




