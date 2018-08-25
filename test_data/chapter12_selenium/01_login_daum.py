from selenium import webdriver

driver = webdriver.Chrome("../../chrome/mac/chromedriver")

driver.get("https://logins.daum.net/accounts/loginform.do?url=http://top.cafe.daum.net/")

login_id = driver.find_element_by_id("id")
login_passwd = driver.find_element_by_id("inputPwd")
login_id.send_keys("oceanfog")
login_passwd.send_keys("")


login_button = driver.find_element_by_id('loginBtn')
login_button.submit()


driver.get("http://cafe.daum.net/ssaumjil/JnwJ")

