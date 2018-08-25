site = {
    "naver": "www.naver.com",
    "google": "www.google.com"
}

print(site.get("naver"))
print(site.get("daum"))

insert_key = "daum"
if (site.get(insert_key) == None):
    print(insert_key + " 에 대한 데이터가 없습니다 ")
