import requests

file = open("./links.txt")
links = file.readlines()

pagenum = 391
for link in links[391:]:
    print("pagenum:", pagenum, "link:", link)
    result = requests.get(link.replace("\n", ""))
    print("status:", result.status_code)
    file2 = open("./sub_pages/" +str(pagenum) + ".html", "w+")
    file2.write(str(result.content))
    pagenum = pagenum + 1

