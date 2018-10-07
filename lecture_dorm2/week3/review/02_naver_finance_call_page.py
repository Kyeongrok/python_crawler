from urllib. request import urlopen

def get_text(url):
    html = urlopen(url)
    return html.read().decode("euc-kr")

url = "https://finance.naver.com/item/main.nhn?code=215600"
html = get_text(url)
print(html)

