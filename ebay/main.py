import ebay.login_and_crawl as crawl
import ebay.allOrdersParser as aop
import ebay.parse_product_info as ppinf


urls = aop.getUrls()

index = 1
for url in urls[0:2]:
    page_string = crawl.getPageString(url)
    result = ppinf.get_order_info(page_string)
    print(result)
    index += 1

