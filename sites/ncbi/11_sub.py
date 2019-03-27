from libs.ncbi import ncbi_crawler as crawler

file = open("/Users/kyeongrok/Desktop/sub_pages2/" + str(int(8180)) +".html")
text = file.read()
res = crawler.getSubPageContent(text)
print(res['authors'])
