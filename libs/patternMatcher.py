import re

# python에서 정규식 쓰기(regular expression)

def findMatchedTexts(text, regexp):
    matched = re.findall(regexp, text)
    return matched