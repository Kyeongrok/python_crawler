import urllib.request

url = "https://t1.daumcdn.net/cfile/tistory/99F4EF335BA2F7321E"
filename = "./hello.jpg"

urllib.request.urlretrieve(url, filename)
