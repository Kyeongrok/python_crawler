from libs import ncbi_crawler as crawler

for page in range(1, 2):
    file = open("./sub_pages/" + str(page) +".html")
    res = crawler.getSubPageContent(file.read())
    print(res['keywords'])
    print(len(res['authors']))
