from bs4 import BeautifulSoup
import libs.dorm_libs.parser_shoppingmall as parser

bs_obj = BeautifulSoup(open("./jolse.html",
                encoding="utf-8").read(), "html.parser")

result = parser.parse(bs_obj)
file = open("./product_infos.csv", "w+")

for item in result:
    file.write(item['name']+","+item['price']+"\n")
file.close()