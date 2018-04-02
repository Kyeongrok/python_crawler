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


def getUrls():

    infos = []
    order_address = []
    for item in tbodys:
        # print(item)
        if( len(item.attrs) != 0):

            if(len(item.attrs['class']) == 2):
                dc_sh_dt_ch = item.find("td", {"class":"dt-sc dt-ch"})
                dc_sh_dt_ch_a = dc_sh_dt_ch.find("a")
                order_address.append(dc_sh_dt_ch_a['href'])
                purchasedQty = item.find("td", {"id": "PurchasedQty"})
                qty = purchasedQty.find("div").text
                infos.append(str(qty))
            elif(len(item.attrs['class']) == 1):
                buyerEmail = item.find("td", {"id": "BuyerEmail"})
                aTag = buyerEmail.find("a")
                infos.append(aTag['title'])

            if(len(infos) == 2):
                infos = []

    return order_address


urls = getUrls()

for url in urls:
    print(url)





