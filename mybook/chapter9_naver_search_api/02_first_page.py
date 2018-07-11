import requests
import bs4
from urllib.parse import urlparse

url = "https://openapi.naver.com/v1/search/blog?query=보험"
result = requests.get(urlparse(url).geturl(), headers={"X-Naver-Client-Id":"VDbFy6nceGqeVmJ5DHmH", "X-Naver-Client-Secret":"bD6e5HDnzX"})

bs_obj = bs4.BeautifulSoup(result.content, "html.parser")

print(bs_obj)