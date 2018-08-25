from selenium import webdriver

driver = webdriver.Chrome("/Users/ydseo/chromedriver")
driver.implicitly_wait(3)

driver.get("https://nid.naver.com/nidlogin.login")

login_id = driver.find_element_by_name("id")
login_passwd = driver.find_element_by_name("pw")
login_id.send_keys("ceoori")
login_passwd.send_keys("z1z1z1")

login_button = driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input')
login_button.click()

driver.get("https://nid.naver.com/user2/help/myInfo.nhn?lang=ko_KR")

