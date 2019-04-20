word = "hello"
price = "1,000"
price2 = "1,000,000"
# l을 a로 바꾸고 싶습니다. 어떻게 해야 할까요?
# .replace()를 검색해서
#  hello -> heaao로 바꿔보세요

replaced = word.replace("l", "a")
print(replaced)
print(price.replace(",",""))
print(price2.replace(",",""))
