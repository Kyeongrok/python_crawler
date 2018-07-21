from urllib.request import urlopen

url = "https://www.naver.com"
html = urlopen(url)

print(html.read())
