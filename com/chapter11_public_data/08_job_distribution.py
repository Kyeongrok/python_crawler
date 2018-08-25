url = endpoint + paramset
result = requests.get(url)
career_data = result.json()
career_list = career_data['dataSearch']['content']

salary_4000_count = 0
salary_4000_profession = {}
for career in career_list:
    if(career['salery'] != 'null'):
        if(int(career['salery'].split(' ')[0]) == 4000):
            salary_4000_count += 1
            key_tmp = career['job_ctg_code']
            if(key_tmp in salary_4000_profession):
                salary_4000_profession[key_tmp] += 1
            else:
                salary_4000_profession[key_tmp] = 1

print("연봉이 4000 만원 이상인 직업의 수 : " + str(salary_4000_count))
print("직업 분류 수 : " + str(len(salary_4000_profession)))
print(salary_4000_profession)

max = 0
majority = ''
for prof in salary_4000_profession:
    tmp = salary_4000_profession[prof]
    if(max < tmp):
        max = tmp
        majority = prof

print("연봉이 4000 만원 이상인 직업 중 가장 많은 직업 코드 : " + str(majority))
