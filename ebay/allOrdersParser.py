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

for item in tbodys:

    if( len(item.attrs) != 0):
        print(item.attrs['class'])
        try:
            buyerEmail = item.find("td", {"id":"BuyerEmail"})
            purchasedQty = item.find("td", {"id": "PurchasedQty"})
            qty = purchasedQty.find("div").text

            aTag = buyerEmail.find("a")
            try:
                productName = aTag['title']
                print(productName)
            except KeyError:
                print(qty)
                pass

        except AttributeError:
            pass





