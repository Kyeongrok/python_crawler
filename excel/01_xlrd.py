import xlrd
from libs.naver_shopping.crawler import crawl
from libs.naver_shopping.parser import parse

workbook = xlrd.open_workbook('user_info.xlsx')
worksheet = workbook.sheet_by_name('db')
list = worksheet._cell_values

for row in list[1:]:
    keyword = row[0]
    result = parse(crawl(keyword))
    print(keyword, result)

