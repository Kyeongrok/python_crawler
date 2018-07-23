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
        <div>
            <ul>
                <li>open</li>
                <li>close</li>
            </ul>
        </div>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# bye 뽑아내기
lis = bs_obj.findAll("li")
print(lis[1].text)

for li in lis[1:2]:
    print(li.text)




