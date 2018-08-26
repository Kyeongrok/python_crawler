import urllib.request
import bs4

def get_bs_obj(url):
    html = urllib.request.urlopen(url)
    bs_obj = bs4.BeautifulSoup(html, 'html.parser')
    return bs_obj


def get_product(cosmetic_category, product_number): #face/42 special/49
    url = 'http://jolse.com/category/'
    url = url + cosmetic_category
    bs_obj = get_bs_obj(url)
    Allproduct_name= bs_obj.findAll('p', {'class':'name'})
    Allproduct_price = bs_obj.findAll('li', {'class': ' xans-record-'})

    print(Allproduct_name[product_number].text, Allproduct_price[product_number*2].text,
          Allproduct_price[product_number*2+1].text)


for product_num in range(0, 50):
    print(get_product('face/42/', product_num ))
