import bs4
str = "<html><div></div></html>"
bsObj = bs4.BeautifulSoup(str, "html.parser")

print(bsObj)