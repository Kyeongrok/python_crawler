from bs4 import BeautifulSoup # 라이브러리 import

# 파일 불러오기
html_text = open("index.html", encoding="utf-8").read()

# BeautifulSoup으로 읽어오기
bsobj = BeautifulSoup(html_text, "html.parser")

# 출력하기
print(bsobj)