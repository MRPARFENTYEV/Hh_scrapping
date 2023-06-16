import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint
import time
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
for vacancy in soup.find_all("a", class_="serp-item__title"):
    links.append(vacancy["href"])

# Переходим по каждой ссылки на страницу вакансии и парсим нужные сведения
for link in links:
    r = requests.get(link, headers=headers.generate())
    print(link)

    soup = BeautifulSoup(r.text, 'lxml')

    # Получаем вилку зарплаты и название компании
    description = soup.find_all("span", class_="bloko-header-section-2 bloko-header-section-2_lite")
    # if len(description) == 2:
    #     # print(description)
    #     print(description[0].text.strip(), description[1].text.strip())
    # #
    # # # Если зарплата не указана, выводим название компании
    # else:
    #     # print(description)
    #     print(description[0].text.strip(), "Зарплата не указана")
    adress_list = []
    # Если длина списка более 1 элемента -> вытаскиваем город регуляркой
    location = soup.find_all("p", attrs={"data-qa": "vacancy-view-location"})

    all_description = soup.find_all("div", class_ ="HH-MainContent HH-Supernova-MainContent")
    for elements in all_description:
        city = re.findall('Москва', str(elements).rstrip())
        city_2 = re.findall('Санкт-Петербург', str(elements).rstrip())
        if elements == city:
            print(city)
        else:

            print(city_2)







    # adress_list.append(loc)


    # for el in adress_list:
    #     print(el)
        # city = re.findall('Москва', str(el).rstrip())
        # city_2 = re.findall('Санкт-Петербург', str(el).rstrip())
        # if el == city:
        #     print(city)
        # elif el == city_2:
        #     print(city_2)
        # else:
        #     print(location[0].text.strip())



# if location:
#     pass
#     # print(location)
#     print(location[0].text.strip())
# else:
#     # print(soup.find_all("span", attrs={"data-qa": "vacancy-view-raw-address"}))
#     loc = soup.find_all("span", attrs={"data-qa": "vacancy-view-raw-address"})
#     adress_list.append(loc)
#     for el in loc:
#         city =re.findall('Москва',str(el).rstrip())
#         print(''.join(city))
#     else:
#         for el in loc:
#             city_2 = re.findall('Санкт-Петербург',str(el).rstrip())
#             print(''.join(city_2))
