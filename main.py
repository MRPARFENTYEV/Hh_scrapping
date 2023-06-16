import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import time
import json
import re

headers = Headers(browser='chrome', os='win')
# Получаем вакансии с первой страницы
url = "https://hh.ru/search/vacancy?text=Python+django+flask&from=suggest_post&salary=&area=1&area=2&ored_clusters=true"
r = requests.get(url, headers=headers.generate())
time.sleep(2)

soup = BeautifulSoup(r.text, 'lxml')

# links = [vacancy["href"] for vacancy in soup.find_all("a", class_="serp-item__title")]
# Получаем ссылки на вакансии

links = []
salary = []
company_title = []
whereabouts = []
for vacancy in soup.find_all("a", class_="serp-item__title"):
    links.append(vacancy["href"])

# Переходим по каждой ссылки на страницу вакансии и парсим нужные сведения
for link in links:

    r = requests.get(link, headers=headers.generate())

    soup = BeautifulSoup(r.text, 'lxml')

    # Получаем вилку зарплаты и название компании
    description = soup.find_all("span", class_="bloko-header-section-2 bloko-header-section-2_lite")
    if len(description) == 2:
        # print(description)
        company_title.append(description[0].text.strip())
        salary.append(description[1].text.strip())
    # Если зарплата не указана, выводим название компании
    else:
        # print(description)
        company_title.append(description[0].text.strip(), )
        salary.append("Зарплата не указана")

    # Если длина списка более 1 элемента -> вытаскиваем город регуляркой
    location = soup.find_all("p", attrs={"data-qa": "vacancy-view-location"})
    city = soup.find('div', attrs={"data-qa": "vacancy-serp__vacancy-address"}).text
    whereabouts.append(city)


# def write(data, filename):
#     data = json.dumps(data)
#     data = json.loads(str(data))
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(data, file, indent= 50)
#
#
# Hh_data = {'Ссылка': links,
#            'Зарплата ': salary,
#            'Название компании': company_title,
#            'Город': whereabouts
#            }
#
# write(Hh_data, 'data.json')
