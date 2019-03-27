from bs4 import BeautifulSoup

html = """
    <html>
        <table>
            <tr>
                <td class='first'>100</td>
                <td>200</td>
            </tr>
            <tr>
                <td>300</td>
                <td>400</td>
            </tr>
        </table>
    </html>
"""

bs_obj = BeautifulSoup(html, "html.parser")
# print(bs_obj)

# 100
td_first = bs_obj.find("td", {"class":"first"})
print(td_first.text)

table = bs_obj.find("table")

# 200
tr = table.find("tr")
tds = tr.findAll("td") # list [ , ,]
print(tds[1].text)


trs = table.findAll("tr")
second_tr = trs[1]

# 300
td_300 = second_tr.find("td")
print(td_300.text)

# 400
second_tr_tds = second_tr.findAll("td")
td_400 = second_tr_tds[1]
print(td_400.text)

# 2 * 2, 3*3, 4*4, 4*5