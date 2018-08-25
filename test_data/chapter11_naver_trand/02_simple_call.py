import json
import requests
from urllib.parse import urlparse

url = "https://openapi.naver.com/v1/datalab/search"
body2 = {"startDate": "2018-01-01",
         "endDate": "2018-04-30",
         "timeUnit": "month",
         "keywordGroups": [{"groupName": "1", "keywords": ["탈잉"]}
                           ],
                            "device": "pc", "ages": ["1", "2"],
                            "gender": "f"}
res = json.dumps(body2)
result = requests.get(urlparse(url).geturl(),
          headers={"X-Naver-Client-Id":"JyP8ZGwBvgwzajxGWs7m",
                   "X-Naver-Client-Secret":"WC3_t8TCMu",
                    "Content-Type":"application/json"
                   },
          data=res.encode("utf-8"))

print(result.json())