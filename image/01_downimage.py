import urllib.request


url = "http://jolse.com/web/product/medium/201809/c3ba634b8a379ed945a9d853d2f7a5a5.jpg"
filename = "./study_room2.jpg"

urllib.request.urlretrieve(url, filename)
