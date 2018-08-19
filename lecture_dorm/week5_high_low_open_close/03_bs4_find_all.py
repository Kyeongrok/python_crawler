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
# 100뽑기
td_first = bs_obj.find("td", {"class": "first"})
# print(td_first.text)

# 200
td_second = bs_obj.find("tr")
second = td_second.findAll("td") # list [ , ,]
print(second[1].text)

#300
td_third = bs_obj.find("table")
ttt = td_third.findAll("tr")
third = ttt[1].find("td")
print(third.text)

#400
td_fourth = bs_obj.find("table")
fourth = td_fourth.findAll("td")
print(fourth[3].text)