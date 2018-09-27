import urllib.request


info = {"url":"http://jolse.com/web/product/medium/201809/c3ba634b8a379ed945a9d853d2f7a5a5.jpg",
        "name":"01.jpg"
        }

urllib.request.urlretrieve(info['url'], info['name'])
