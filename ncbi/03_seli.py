from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../chrome/mac/chromedriver")
url = "https://www.ncbi.nlm.nih.gov/pubmed/?term=(%22Acute+Myeloid+Leukemia%22)+OR+%22AML%22"
print(url)
driver.get(url)
driver.find_element_by_xpath("//*[@id=\"result_action_bar\"]/ul/li[3]").click()

wait = WebDriverWait(driver, 10)
wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="display_settings_menu_ps"]/fieldset/ul/li[6]/label'))
)
# 200선택
driver.find_element_by_xpath('//*[@id="display_settings_menu_ps"]/fieldset/ul/li[6]/label').click()

wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div/div[5]/div[200]/div[2]/p/a'))
)

# 저장
file = open("./1.html", "w+")
file.write(driver.page_source)


def clickAndWaitAndSave(pageNum):
    print("pageNum:", pageNum)

    wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div/div[5]/div[200]/div[2]/p/a'))
    )
    file = open("./links_page/"+str(pageNum)+".html", "w+")
    file.write(driver.page_source)

    inputElement = driver.find_element_by_xpath('//*[@id="pageno"]')
    inputElement.clear()
    inputElement.send_keys(str(pageNum))
    inputElement.send_keys(Keys.ENTER)

for num in range(2, 195):
    clickAndWaitAndSave(num)

driver.close()

