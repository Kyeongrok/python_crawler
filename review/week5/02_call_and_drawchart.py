from urllib.request import urlopen
import json
import matplotlib.pylab as plt

url = "http://grains.krei.re.kr/chart/main_chart/index/kind/S/sdate/2018-01-01/edate/2018-05-05"
html = urlopen(url)

json_obj = json.load(html)
x = []
y = []

# 차트 그리기 2018-01-01 ~ 2018-05-05까지 데이터로
# x축은 날짜, y축은 가격

for item in json_obj:
    # print(item)
    # date, settlement 나오게 해보세요.
    x.append(item['date'])
    y.append(item['settlement'])
    print(item['date'] + "," +item['settlement'])

print(x)
print(y)

plt.plot(x, y)
plt.show()