import requests
from bs4 import BeautifulSoup
import pandas as pd


#делаем запрос к сайту
url = 'https://yummyani.me/catalog/top'
page = requests.get(url)
print(f'Статус: {page.status_code}')


#создаем списки
filteredNews = []
allNews = []
allRate = []
fillteredRare = []


#настройка BeautifulSoup
soup = BeautifulSoup(page.text, "html.parser")


#ищем и помещаем в список элементов с названием аниме
allNews = soup.findAll('a',class_='anime-title')


#метод для списка чтобы в нем был только текст
for data in allNews:
        filteredNews.append(data.text)


#добавление в список элементы сколько просмотров
allRate = soup.findAll('div', class_='views-count')

#фильтруем
for rating in allRate:
        fillteredRare.append(rating.text)

list = []
#вывод
n = 1
i = 0
for names in filteredNews:
        print(f"{n}.{names} |просмотров: {fillteredRare[i]} ")
        n += 1
        i += 1
list = []
for a in filteredNews:
        list.append(a)

list1 = pd.DataFrame(list)
list1.to_csv('TEST')




