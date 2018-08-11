import urllib.request
import bs4

# url을 받아서 bs_obj를 return하는 function
# 으로 만들어보세요

def get_bs_obj(url):
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, "html.parser")
    return bs_obj
url="https://www.naver.com"
bs_obj = get_bs_obj(url)
to_start = bs_obj.find("a",{"data-clk":"top.mkhome"})
print(to_start.text)