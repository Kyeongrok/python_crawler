from selenium import webdriver
import ebay.login_and_crawl as crawl
import ebay.allOrdersParser as aop

order_list_url_template = lambda page_num: "https://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&pageNumber={}".format(page_num)

# 2+1=1~2, 3+1=1~3
for index in range(1,2+1):
    order_list_url = order_list_url_template(index)
    order_list_page_string = crawl.getPageString(order_list_url)
    urls = aop.getUrls(order_list_page_string)

    driver = webdriver.Chrome('../chrome/mac/chromedriver')
    crawl.getPageString2(driver, urls)
