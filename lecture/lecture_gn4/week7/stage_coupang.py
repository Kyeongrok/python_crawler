from libs.coupang.productTotalCountGetter import getKeywordTotalCount
from libs.coupang.productGetter import getKeywordResults

totalCount = getKeywordTotalCount("마카롱")
iTotalCount = int(totalCount)
print(iTotalCount)
print(type(iTotalCount))

endPage = iTotalCount // 36
print("endPage:", endPage)

results = getKeywordResults("마카롱", 50)
print(len(results))

import json
file = open("./macaron.json", "w+")
file.write(json.dumps(results))