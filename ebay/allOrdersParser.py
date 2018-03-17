from bs4 import BeautifulSoup

fileName = "./allorders.html"
def printLineByLine(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.read()
        return line


result = printLineByLine(fileName)
# print(result)
bsObj = BeautifulSoup(result, "html.parser")
content = bsObj.find("table", {"id":"content"})
mu_active_tbl_id = content.find("div", {"id":"mu_active_tbl_id"})
tbodys = mu_active_tbl_id.findAll("tbody")

infos = []
for item in tbodys:
    if( len(item.attrs) != 0):

        if(len(item.attrs['class']) == 2):
            purchasedQty = item.find("td", {"id": "PurchasedQty"})
            qty = purchasedQty.find("div").text
            infos.append(str(qty))
        elif(len(item.attrs['class']) == 1):
            buyerEmail = item.find("td", {"id": "BuyerEmail"})
            aTag = buyerEmail.find("a")
            infos.append(aTag['title'])

        if(len(infos) == 2):
            print(infos)
            infos = []





