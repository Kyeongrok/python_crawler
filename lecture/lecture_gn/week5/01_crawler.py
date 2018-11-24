import requests

url = "http://jolse.com/category/eyebrow/68/?page=1"
result = requests.get(url)

file = open("./eyebrow_1.html","w+")
file.write(str(result.content))
