import requests

def crawl(categoryNo, pageNo):
    url = "https://www.coupang.com/np/categories/{}?page={}".format(categoryNo, pageNo)
    data = requests.get(url)
    print(url, data)
    return data.content


