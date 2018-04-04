import ebay.login_and_crawl as crawl
import ebay.allOrdersParser as aop
import ebay.parse_product_info as ppinf


order_list_url_template = lambda page_num: "https://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&pageNumber={}".format(page_num)
order_list_urls = [order_list_url_template(1)
    , order_list_url_template(2)]

order_list_page_string = crawl.getPageString(order_list_urls[0])
print(order_list_page_string)
urls = aop.getUrls(order_list_page_string)


for url in urls:
    item_page_string = crawl.getPageString(url)
    result = ppinf.get_order_info(item_page_string)
    print(result)

