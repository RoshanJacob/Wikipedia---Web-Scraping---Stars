from bs4.builder import TreeBuilderRegistry
import requests
from bs4 import BeautifulSoup
import csv
import time


GET_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# 98 Tables in the html page
scraped_data = []
d = []
headers = ['Name', 'Distance', 'Mass', 'Radius', 'Luminosity']


def scraper():

    requestToWeb = requests.get(GET_URL)

    # for each in range(1, 2):
    garlicSoup = BeautifulSoup(requestToWeb.content, 'html.parser')

    superscript = garlicSoup.find_all('sup')
    span = garlicSoup.find_all('span')

    for s in superscript:
        s.decompose()

    for sp in span:
        sp.decompose()

    # table = garlicSoup.find_all('table', attrs = {'class', 'wikitable sortable jquery-tablesorter'})

    for index1, each_tr in enumerate(garlicSoup.find_all('tr')):
        temp_list = []

        td_items = each_tr.find_all('td')

    # print(td_items)

        for index, item in enumerate(td_items):
            if index == 1:
                try:
                    temp_list.append(item.find_all('a')[0].contents[0])
                except:
                    # try:
                    temp_list.append(item.contents[0])
                    # except:
                    #     temp_list.append(item.content[0])
            elif index == 3:
                try:
                    temp_list.append(item.contents[0] + ' ' + 'Light-Years')
                except:
                    print('AGH!')
            elif index == 5:
                try:
                    if item.contents[0] == '?':
                        temp_list.append('Un-referred')
                    else:
                        temp_list.append(item.contents[0])
                except:
                    print("Whoops.")
            elif index == 6:
                try:
                    temp_list.append(item.contents[0])
                except:
                    print("AHA!")
            elif index == 7:
                try:
                    temp_list.append(item.contents[0])
                except:
                    print('???')
        print(temp_list)
        scraped_data.append(temp_list)


scraper()


for index, items in enumerate(scraped_data):
    newElement = scraped_data[index]
    newElement = [item.replace('\n', '') for item in newElement]
    newElement = newElement[:]

    d.append(newElement)

with open('GottenStarData.csv', 'w', encoding='utf-8') as j:
    writer = csv.writer(j)
    writer.writerow(headers)
    writer.writerows(d)
