import requests

url = 'http://localhost:8080/api/v1/order/distribute?id=1111&name=krk'
res = requests.get(url, headers={
    'X-USER-ID':'oceanfog'
})

print(res.content)

