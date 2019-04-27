import os
from selenium import webdriver

dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
driver = webdriver.Chrome(
    executable_path="{}/bin/chromedriver".format(dir_path),
)

url = "https://coupang.co.kr/"
driver.get(url)

