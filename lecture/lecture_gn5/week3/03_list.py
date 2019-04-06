# list의 특징 for문을 쓸 수 있다.
# 순서를 가지고 접근을 합니다.
# 0번부터 시작
# [] 대괄호
list = [1, 2, 3, 4]
list2 = [
         1,
         2,
         3
         ]

# print(list)
# print(list2)
# print(list2[1])

strList = ["americano", "latte", "케익1", "티1", "티2"]
# print(strList)

dictList = [
    {"name":"한국전력", "price":"29200", "location":"한국"},
    {"name":"sk하이닉스", "price":"79800", "location":"이천"},
    {"name":"풍산", "price":"12900", "location":"충정로"},
]

# for each
# 회사 0000은 현재 가격이 000원이고 aaa에 위치해있습니다.
for company in dictList:
    message2 = "회사 {}은 현재 가격이 {}원이고 {}에 위치해있습니다."\
        .format(company['name'],company['price'], company['location'])
    print(message2)