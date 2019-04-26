from libs.crawler import crawl
from libs.browser import Browser

url = "https://www.instagram.com/explore/tags/댕스타그램"


browser = Browser()
browser.move(url)
ele_a_datetime = browser.find_one('.e02As .c-Yi7', 5)
print(ele_a_datetime)
