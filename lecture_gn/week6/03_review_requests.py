import requests

# url을 가지고 str
url = "http://jolse.com/category/cleansing/58/"
def crawl(url, fileLocationName):
    result = requests.get(url)
    file = open(fileLocationName, "w+")
    file.write(str(result.content))

crawl(url, "./jolse_02.html")
