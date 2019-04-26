import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

class Browser:
    def __init__(self):
        print("--------init------")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        service_args = ['--ignore-ssl-errors=true']
        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            executable_path="{}/bin/chromedriver".format(dir_path),
            service_args=service_args,
            chrome_options=chrome_options
        )
        self.driver.implicitly_wait(5)


    def move(self, url):
        self.driver.get(url)

    def find_one(self, css_selector, elem=None, waittime=0):
        obj = elem or self.driver

        if waittime:
            WebDriverWait(obj, waittime).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )

        try:
            return obj.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            return None

