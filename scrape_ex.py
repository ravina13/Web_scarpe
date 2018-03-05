import requests
from bs4 import BeautifulSoup

quote_page = requests.get("https://www.builtinnyc.com/jobs?f[0]=job-category_data-analytics")

soup = BeautifulSoup(quote_page.text,'html.parser')

title_box = soup.find('h2', attrs={'class' : 'title'})
title = title_box.text.strip()
print(title)

company_box = soup.find('div', attrs={'class' : 'company-title'})
company = company_box.text.strip()
print(company)

import csv
with open ('index1.csv', 'a') as filecsv:
	writer = csv.writer(filecsv)
	writer.writerow([title,company])


