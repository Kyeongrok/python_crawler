from selenium import webdriver
from bs4 import BeautifulSoup

def getPageString(url):
    driver = webdriver.Chrome('../chrome/mac/chromedriver')
    driver.implicitly_wait(3)

    driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=')
    driver.find_element_by_name('userid').send_keys('jackpiros909@gmail.com')
    driver.find_element_by_name('pass').send_keys('claeo1@3')  # 사용할 패스워드
    driver.find_element_by_name('pass').submit()
    driver.get(url)


    html = driver.page_source
    driver.close()
    encodedHtml = html.encode('utf-8')

    return html

def saveToFile():
    html = getPageString('https://k2b-bulk.ebay.com/ws/eBayISAPI.dll?SalesRecordConsole&currentpage=SCSold&ssPageName=STRK:ME:LNLK')

    with open("./allorders.html", encoding="utf-8", mode="w+") as f:
        f.write(str(html))
