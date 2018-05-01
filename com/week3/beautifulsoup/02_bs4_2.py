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
