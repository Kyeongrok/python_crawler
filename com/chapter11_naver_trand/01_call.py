#-*- coding: utf-8 -*-
import urllib.request
import json
import requests
from urllib.parse import urlparse

client_id = "JyP8ZGwBvgwzajxGWs7m"
client_secret = "WC3_t8TCMu"
url = "https://openapi.naver.com/v1/datalab/search"
body2 = {"startDate": "2018-01-01",
         "endDate": "2018-04-30",
         "timeUnit": "month",
         "keywordGroups": [{"groupName": "1", "keywords": ["탈잉"]}
                           ],
                            "device": "pc", "ages": ["1", "2"],
                            "gender": "f"}
res = json.dumps(body2)



request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=res.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

