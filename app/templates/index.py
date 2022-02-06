import requests
from bs4 import BeautifulSoup
url = 'https://yandex.ru/maps/org/moskovskiy_universitet_im_s_yu_vitte_fakultet_upravleniya/1384213316/reviews/?ll=37.655135%2C55.700335&z=8'
data = requests.get(url)
data.text
result = BeautifulSoup(data.text, 'lxml')
quotes = result.find_all('span', class_='business-review-view__body-text')
authors = result.find_all('div', class_='business-review-view__author')
for div in result.find_all("div", {'class':'business-review-view__author-profession'}): 
    div.decompose()
for i in range(0, len(quotes)):
  print(quotes[i].text)
   #print(quotes[i].text)
  print('***************************************')
  print('--' + authors[i].text)
    



