from urllib.request import urlopen

url = "http://grains.krei.re.kr/chart/main_chart/index/kind/W/sdate/1972-01-01/edate/2018-04-28"
text = urlopen(url)

print(text.read())