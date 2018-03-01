from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/Users/ydseo/chromedriver')
driver.implicitly_wait(3)

driver.get('https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=')

driver.find_element_by_name('userid').send_keys('ydseo2015@gmail.com')
driver.find_element_by_name('pass').send_keys('') # 사용할 패스워드

driver.find_element_by_name('pass').submit()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

print(html)

driver.close()