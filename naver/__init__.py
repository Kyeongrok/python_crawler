from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('../chrome/mac/chromedriver')
driver.implicitly_wait(3)

driver.get('https://www.naver.com/')

driver.find_element_by_name('id').send_keys('oceanfog2')
driver.find_element_by_name('pw').send_keys('') # 사용할 패스워드

driver.find_element_by_css_selector('.login .btn_login input').submit()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

encodedHtml = html.encode('utf-8')
print(encodedHtml)

driver.close()