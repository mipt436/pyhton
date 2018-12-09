import requests
from BeautifulSoup import BeautifulSoup

s = requests.session()
respond = s.get('https://lenta.ru/news/2018/11/28/imena/')
bs = BeautifulSoup(respond.content)
print bs.find(itemprop="articleBody").text
