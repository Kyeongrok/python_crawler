import requests
from bs4 import BeautifulSoup
url = "https://display.ellotte.com/display-fo/:filter"
result = requests.post(url,headers={"cookie":"JSESSIONID=acaf0dda-a2e5-4d0d-8469-24cd1f58b9d5; lotte40UniqUserKey=1543735743058_73997; _ga=GA1.2.49650136.1543735743; _gid=GA1.2.1438045983.1543735743; _fbp=fb.1.1543735743313.1311080027; cto_lwid=c4d20f21-7ec7-486c-9274-fa39e8a4c3ad; alido_pcid=sOkOuhJNoJmUqsMIkNF96; alido_agree=Y; _gac_UA-116499776-2=1.1543735744.Cj0KCQiA_4jgBRDhARIsADezXchZ8TA4o2Czo7I8uD4JPH3tA_2-fg_C1shQ3ZH-JJ6o7Y70TBnoP5caAmblEALw_wcB; EL_RECENT_SHOPPING_INFOMATION=2%3ABag%26Acc+%3E+%EC%8A%88%EC%A6%88%3A10023%7C%7C2%3AShoes+%3E+%EB%82%A8%EC%84%B1%ED%99%94%3A10051%7C%7C; _gat_UA-116499776-2=1"},
                       params={"query":"","realQuery":"","pageNo":"","pageCnt":"40","collection":"","reQuery":"","sort":"01","catgId":"10001$10003$10023","brandId":"","rating":"","minPrice":"","maxPrice":"","attr":"","coupon":"","sale":"","dlvType":"","interestFree":"","deal":"","smartPick":"","duplChk":"","exhibitionId":""})
print(result)
