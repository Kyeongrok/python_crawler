from libs.NaverFinance.crawl import crawl
from libs.NaverFinance.parser import getCompanyInfo

#025980 아난티, 000660 sk하이닉스

codes = ["000660", "025980", "005930"] # 종목코드표

for code in codes:
    print(getCompanyInfo(crawl(code)))

