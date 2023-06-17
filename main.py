import json
import csv
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import time
import re

all_links = 'https://hh.ru/search/vacancy?area=1&area=2&search_field=name&search_field=company_name&search_field=description&enable_snippets=false&text=python+%2B+flask'
headers = Headers(browser='chrome', os='win')
req = requests.get(all_links, headers=headers.generate())
time.sleep(2)
soup = BeautifulSoup(req.text, 'lxml')
results = soup.find_all('div', class_='serp-item')

titles =[]
links =[]
payment =[]
whereabouts =[]
parsed_data =[]


for res in results:
    title = res.find("a", class_="serp-item__title").text
    titles.append(title)
    hrefs = res.find("a", class_="serp-item__title").get('href')
    links.append(hrefs)
    salary_find = res.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})

    if salary_find:
        salary = salary_find.text
        payment.append(salary)

    else:
        salary = 'з/п не указана'
        payment.append(salary)


    city = soup.find('div', attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
    parsed_data.append(
        {'links' : hrefs,
         'title' : title,
         'salary' : salary,
         'city' : city
         }
    )

def write_file(data,filename):
    data = json.dumps(data)
    data = json.loads(str(data))

    with open (filename,'w', encoding='utf8') as f:
        json.dump(data, f, indent=3)
write_file(parsed_data,'parsed_data.json')








