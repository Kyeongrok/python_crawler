import requests
def crawl(url, fileLocationName):
    # url을 받아서
    # request를 하고 str
    result = requests.get(url)
    # 결과를 파일로 저장
    print(result.content)
    saveToFile(result.content, fileLocationName)

def saveToFile(str1, fileLocationName):
    # file에 저장
    file = open(fileLocationName, "w+")
    file.write(str(str1))
