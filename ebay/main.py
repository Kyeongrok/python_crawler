import ebay.login_and_crawl as crawl
import ebay.allOrdersParser as aop
import ebay.parse_product_info as ppinf


order_list_url = lambda page_num: "https://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&pageNumber={}".format(page_num)



print(order_list_url(1))
print(order_list_url(2))

# urls = aop.getUrls()
#
# index = 1
# for url in urls[0:2]:
#     page_string = crawl.getPageString(url)
#     result = ppinf.get_order_info(page_string)
#     print(result)
#     index += 1

