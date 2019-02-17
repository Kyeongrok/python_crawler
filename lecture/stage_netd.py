from libs.netd.netd_crawler import getLinks

links = []
for num in range(0, 2):
    links = links + getLinks(num * 10 + 1)
print(len(links))