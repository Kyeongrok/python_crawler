import urllib.request

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

print(html.read())