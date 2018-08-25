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
result = requests.get(url)
career_data = result.json()
career_list = career_data['dataSearch']['content']

salary_4000_count = 0
for career in career_list:
    if(career['salery'] != 'null'):
        if(int(career['salery'].split(' ')[0]) == 4000):
            salary_4000_count += 1

print("연봉이 4000 만원 이상인 직업의 수 : " + str(salary_4000_count))
