import requests

url = "http://jolse.com/category/wash/56/"

result = requests.get(url)

print(result) # 200 is Ok Success
print(result.content)