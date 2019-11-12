from sites.unipass import parse
from libs.crawler import crawl


url = "https://unipass.customs.go.kr/csp/index.do"

result = crawl(url)
parse(result)
