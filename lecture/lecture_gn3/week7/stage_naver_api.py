from libs.naver_api.crawler import crawl

apiResult = crawl("강남역 평양 냉면")

items = apiResult['items']

print(len(items))
print(items[0])