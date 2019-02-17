from libs.naver.crawler import crawl
from libs.naver.parser import parse

# 무대 -> 배우, 장치, 조명
# crawl호출 parse호출 결과 출력
code = "000660"
string = crawl(code)
companyInfo = parse(string)
print(companyInfo)