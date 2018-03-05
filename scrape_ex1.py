import requests
from bs4 import BeautifulSoup

quote_page = requests.get("http://us.shein.com/US-Clothing-vc-34769.html?icn=clothing&ici=us_navbar04")

soup = BeautifulSoup(quote_page.text,'html.parser')

print (soup.prettify())
#originals = soup.findAll("div", {"class" : "c-goodsli j-goodsli j-itemtpl col-lg-3 col-sm-4 col-xs-6"})


#print(len(originals))

#title_box_list = title_box.find_All('div')




