import requests
import bs4

url = "http://jolse.com/category/tonermist/43/"
result = requests.get(url)

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

print(bs_obj)