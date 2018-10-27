import dorm_libs.crawler as crawler

list = [
{"code":"060310","name":"3S"},
{"code":"095570","name":"AJ네트웍스"},
{"code":"068400","name":"AJ렌터카"},
{"code":"006840","name":"AK홀딩스"},
{"code":"054620","name":"APS홀딩스"},
{"code":"265520","name":"AP시스템"},
{"code":"211270","name":"AP위성"},
{"code":"152100","name":"ARIRANG 200"},
{"code":"222170","name":"ARIRANG S&P한국배당성장"},
{"code":"161490","name":"ARIRANG 경기방어주"},
{"code":"161500","name":"ARIRANG 경기주도주"},
{"code":"161510","name":"ARIRANG 고배당주"}
    ]

for item in list:
    try:
        price = crawler.getPrice(item['code'])
        print(item['name'], price)
    except:
        print(item['name'], "error") #10400
