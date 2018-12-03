import requests
from bs4 import BeautifulSoup
from xmljson import badgerfish as bf
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
params = '?' + \
    'LAWD_CD=' + '11110' +\
    '&DEAL_YMD=' + '201512' + \
    '&serviceKey=' + 'QOIyVxx7oVtU%2B03Na7PG6BWsVsElYmp8921ouUzpePsIOHFnNAOXhlYy4lrwBeG31dKKRfdKRmTY2CY034o2qw%3D%3D'

url = url + params
result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
items = bs_obj.find("item")
print(items)
