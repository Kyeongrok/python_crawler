import bs4
html_str = '<html><div>hello</div></html>'
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(bs_obj)
print(bs_obj.find("div"))
print(bs_obj.find("div").text)
