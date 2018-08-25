site = {
    "naver": "www.naver.com",
    "google": "www.google.com",
    "daum": "www.daum.net"
}

print(site.keys())
print(site.values())
print(site.items())

for key in site.keys():
    print(key)
for value in site.values():
    print(value)
for item in site.items():
    print(item)
