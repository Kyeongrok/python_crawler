# keywordResult
products = [
    {"name":"바디워시1", "price":1000},
    {"name":"바디워시2", "price":2000}
]

import json
file = open("result.json", "w+")
file.write(json.dumps(products))
