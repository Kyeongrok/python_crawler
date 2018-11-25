#1.Naver Api호출하기
#2.lib로 분리하기
#3.lib import하기
#4.bloggername, title, link추출하기
#5.result.csv로 저장하기

import gn_lib3.api_call as apicall

result = apicall.naverApiCall("역삼역 공연")
print(result)