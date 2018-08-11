from selenium import webdriver

driver = webdriver.Chrome("../../chrome/mac/chromedriver")

driver.get("https://nid.naver.com/nidlogin.login")

driver.implicitly_wait(3)
login_id = driver.find_element_by_id("id")
login_passwd = driver.find_element_by_id("pw")
login_id.send_keys("oceanfog")
login_passwd.send_keys("")

login_button = driver.find_element_by_class_name('btn_global')
login_button.click()
