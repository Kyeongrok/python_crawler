import requests
from bs4 import BeautifulSoup
url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
queryParams = '?' + 'LAWD_CD=' +'11110' \
              + '&DEAL_YMD=' + '201811' \
              + '&serviceKey=' + 'QOIyVxx7oVtU%2B03Na7PG6BWsVsElYmp8921ouUzpePsIOHFnNAOXhlYy4lrwBeG31dKKRfdKRmTY2CY034o2qw%3D%3D'

url = url + queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)