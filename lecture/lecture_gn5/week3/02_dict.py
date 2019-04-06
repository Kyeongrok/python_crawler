# dictionary 딕셔너리 dict 사전
# price : 가격 물건이나 서비스의 가격, 대가 이런 의미로도 쓰인다
# {key:value}

# 특정 종목(한국전력)을 dict로 표현 해보세요
# 이름, 가격, 코드, 시가총액, 시가, 고가, 저가
company = {"name":"한국전력", "price":"29200", "code":"112345",
           "total":"1800000000", "open":"29900", "high":"30150",
           "low":"29100"}
print(company)
print(company['name'], company['code'])