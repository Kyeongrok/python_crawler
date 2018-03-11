from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chromedriver')
driver.implicitly_wait(3)

driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=')

driver.find_element_by_name('userid').send_keys('jackpiros909@gmail.com')
driver.find_element_by_name('pass').send_keys('') # 사용할 패스워드

driver.find_element_by_name('pass').submit()

driver.get('https://www.ebay.com/sh/ovw')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

encodedHtml = html.encode('utf-8')
print(encodedHtml)

with open("./hello.html", encoding="utf-8", mode="w+") as f:
    f.write(str(html))


driver.close()