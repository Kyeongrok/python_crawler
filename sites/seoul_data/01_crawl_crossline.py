import requests, json
import pandas as pd

results = []

for i in range(1):
    url = 'http://openapi.seoul.go.kr:8088/{}/json/SdeA004A1W/1/1000/'.format('65764641776f63653131306347675750')
    # 1 1000       1000 * i + 1    1000 * i
    # 1001 2000
    print(url)

    string = requests.get(url).content
    print(string)
    jso = json.loads(string)
    result = jso['SdeA004A1W']['row']
    print(len(result))
    df = pd.DataFrame(result)
    df.to_excel('cross_line.xlsx')
