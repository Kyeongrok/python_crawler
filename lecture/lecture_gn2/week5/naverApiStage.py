# lib import하기
import json
from libs.naver.apiCrawler import crawl

def getSearchResults(keyword):
    results = []
    for num in range(0, 10):
        items = crawl(keyword, 100 * num + 1)['items']
        print(items)
        results += items
    return results

results = getSearchResults("강남역 저녁")

file = open("./results.json", "w+")
file.write(json.dumps(results))
