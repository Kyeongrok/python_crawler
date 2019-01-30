import requests
from unipass.parser import parse
from libs.crawler import crawl


url = "https://unipass.customs.go.kr/csp/index.do"

result = crawl(url)
parse(result)
