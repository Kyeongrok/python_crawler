from selenium import webdriver

driver = webdriver.Chrome("../../chrome/mac/chromedriver")

driver.get("http://www.kofiabond.or.kr/websquare/websquare.html?w2xPath=/xml/Com/Common_TabMnuDsp.xml&divisionId=MBIS01070010000000&serviceId=BIS0100100280&topMenuIndex=6&w2xHome=/xml/&w2xDocumentRoot=")

table = driver.title

print(table)
print(driver.find_element_by_tag_name("div").text)
