import requests

endpoint = "http://www.career.go.kr/cnet/openapi/getOpenApi?"
apiKey = "5acdf05d7a4fe0f7d21c0770379c705e"
svcType = "api"
svcCode = "JOB"
contentType = "json"
gubun = "job_dic_list"
perPage = "10000"

paramset = "apiKey=" + apiKey + "&" + "svcType=" + svcType + "&" + "svcCode=" + svcCode + \
           "&" + "contentType=" + contentType + "&" + "gubun=" + gubun + "&" + "perPage=" + perPage

url = endpoint + paramset
print(url)
result = requests.get(url)
career_data = result.json()
print(type(career_data))
print(type(career_data['dataSearch']))
print(type(career_data['dataSearch']['content']))
print(len(career_data['dataSearch']['content']))
