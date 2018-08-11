from selenium import webdriver

driver = webdriver.Chrome("../../chrome/mac/chromedriver")
driver.implicitly_wait(3)

driver.get("https://nid.naver.com/nidlogin.login")

login_id = driver.find_element_by_name("id")
login_passwd = driver.find_element_by_name("pw")
login_id.send_keys("아이디")
login_passwd.send_keys("비밀번호")

login_button = driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input')
login_button.click()
