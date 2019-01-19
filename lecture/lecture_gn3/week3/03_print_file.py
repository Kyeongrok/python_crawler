from libs.NaverFinance.crawl import crawl
from libs.NaverFinance.parser import getCompanyInfo

file = open("./codes.csv")
lines = file.readlines()
print(lines)
for line in lines:
    code = line.replace("\n", "")
    print(getCompanyInfo(crawl(code)))

