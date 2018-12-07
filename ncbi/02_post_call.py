from libs import ncbi_crawler as crawler


links = []

for num in range(0, 195):
    start = num * 200 + 1
    links = links + crawler.getNetdLinks(str(start))

file = open("./links.txt", "w+")
for link in links:
    file.write(link + "\n")
