import ebay.login_and_crawl as crawl
import ebay.allOrdersParser as aop



urls = aop.getUrls()

index = 1
for url in urls[0:2]:
    page_string = crawl.getPageString(url)
    print(page_string)
    with open("./eachPage{}.html".format(index), encoding="utf-8", mode="w+") as f:
        f.write(str(page_string))

    index += 1

