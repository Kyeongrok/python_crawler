import gn_lib3.naver_api_caller as caller

file = open("./result.csv", "w+")
result = caller.call("강남역 공연", 1)
print(result)
for item in result['items']:
    print(item)
     # file.write(item['title'] + "@" +
     #            item['bloggername'] + "\n")
