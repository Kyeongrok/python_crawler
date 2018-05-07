from selenium import webdriver

driver = webdriver.Chrome('../../chrome/mac/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.amazon.com/Best-Sellers/zgbs")

html = driver.page_source
print(html)
driver.close()

