from bs4 import BeautifulSoup



fileName = "./eachPage1.html"
def getFileString(file_path):
    with open(file_path, 'rt', encoding='utf-8') as f:
        line = f.read()
        return line

def get_order_info(page_string):
    bsObj = BeautifulSoup(page_string, "html.parser")
    tbody = bsObj.find("tr", {"class":"shreskin-edit-sales-record-buyer-details"}).find("table").find("tbody").find("table").find("tbody")
    trs = tbody.findAll("tr")

    id = trs[0].findAll("td")[1].find("b").text
    email = trs[1].findAll("td")[1].find("b").text
    buyer_full_name = trs[3].findAll("td")[1].find("input")['value']
    street1 = trs[4].findAll("td")[1].find("input")['value']
    street2 = trs[5].findAll("td")[1].find("input")['value']
    city = trs[6].findAll("td")[1].find("input")['value']
    print(buyer_full_name)

    result = "{},{},{},{},{},{}"\
        .format(id, email, buyer_full_name, street1, street2, city)
    return result

result = get_order_info(getFileString(fileName))
print(result)

