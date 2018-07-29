import requests
import bs4

# url을 넣으면 해당 페이지의 bs_obj을 return하는
# get_page_from_url이라는 함수를 만들어 보세요
def get_page_from_url(url):
    result = requests.get(url)
    bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
    return bs_obj

url = "http://jolse.com/category/tonermist/43/"
print(get_page_from_url(url))