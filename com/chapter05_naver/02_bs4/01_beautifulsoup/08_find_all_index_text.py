import bs4

html_str = """
<html>
    <body>
        <ul>
            <li>apple</li>
            <li>carrot</li>
            <li>tomato</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(lis[1])
print(type({}))

for i in range(0, 10):
    for j in range(1, 10):
        print("hello")