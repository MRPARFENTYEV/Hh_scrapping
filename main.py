import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from pprint import pprint

headers = Headers(browser='chrome', os='win')
url = 'https://nahabino.hh.ru/search/vacancy?text=Python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&ored_clusters=true'
r = requests.get(url, headers=headers.generate()).text
# print(r)
soup = BeautifulSoup(r, 'lxml')
name = soup.find('h3', class_= 'bloko-header-section-3').find('a', class_='serp-item__title').text

# link = soup.find('h3', class_= 'bloko-header-section-3').find('a', class_='serp-item__title').get('href')
# description = soup.find('div',class_='HH-MainContent HH-Supernova-MainContent').find('div',class_='vacancy-description')
# description = soup.find('div',class_='HH-MainContent HH-Supernova-MainContent').
# print(description)

# print(description)


filter_1 = []
profession_title = soup.find('h3', class_='bloko-header-section-3').find('a', class_='serp-item__title').text

profession_titles = soup.find_all('h3', class_='bloko-header-section-3')

for profession in profession_titles:
    filter_1.append(profession)
    # link = profession.find('a', class_='serp-item__title').get('href')


filter_2 = []
for raw in filter_1:
    if 'По вашему запросу ещё будут появляться новые вакансии. Присылать вам?' not in raw:
        filter_2.append(raw)
parsed_list = []
for elements in filter_2:
    if 'Быстрые фильтры' not in elements:
        parsed_list.append(elements)
pre_final_list = []
for lines in parsed_list:
    if 'Как вам результаты поиска?' not in pre_final_list:
        pre_final_list.append(lines)

for links in pre_final_list:
    if None in links:
        continue
    else:
        link = links.find('a', class_='serp-item__title').get('href')
        titles = links.find('a', class_='serp-item__title').text


    print(f"{titles}:{link}")


