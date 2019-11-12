import time
import random
from selenium import webdriver
from bs4 import BeautifulSoup


## Selenium methods
# URL에 접근하는 api,

# get('http://url.com')
# 페이지의 단일 element에 접근하는 api,

# find_element_by_name('HTML_name')
# find_element_by_id('HTML_id')
# find_element_by_xpath('/html/body/some/xpath')
# 페이지의 여러 elements에 접근하는 api 등이 있다.

# find_element_by_css_selector('#css > div.selector')
# find_element_by_class_name('some_class_name')
# find_element_by_tag_name('h1')

## PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS(
#     "/Users/jihyun/Documents/GitHub/Python-Selenium-crawler-naver/phantomjs-2.1.1-macosx/bin/phantomjs"
# )


options = webdriver.ChromeOptions()

options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
)
options.add_argument("lang=ko_KR")

## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# driver = webdriver.Chrome(
#     "/Users/jihyun/Documents/GitHub/Python-Selenium-crawler-naver/chromedriver",
#     chrome_options=options,
# )

driver = webdriver.Chrome("../../chrome/mac/chromedriver")
time.sleep(5 + random.random() * 0.3)

## 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
# driver.implicitly_wait(3)

## url에 접근한다.
driver.get("https://nid.naver.com/nidlogin.login")

time.sleep(5 + random.random() * 0.3)

## 아이디/비밀번호를 입력해준다.
driver.find_element_by_name("id").send_keys("stothyu&&**ni")
time.sleep(5 + random.random() * 0.3)

driver.find_element_by_name("pw").send_keys("gos^dk**^^di1")
time.sleep(5 + random.random() * 0.3)

## 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(15)

# Naver 메일 들어가기
driver.get("https://mail.naver.com/?n=1552402737365&v=f")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Naver 메일 뽑아 내기
notices = soup.findAll("strong", {"class": "mail_title"})

for n in notices:
    print(n.text.strip())
time.sleep(2)