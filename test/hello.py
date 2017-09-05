#https://www.digitec.ch/de/s1/producttype/tv-4?tagIds=538

#http://www.melectronics.ch/c/de/TV_%26_Audio/Fernseher/

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.digitec.ch/de/s1/product/sony-kdl-32rd435-32-wxga-lcd-tv-5713966?tagIds=538")
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj)

