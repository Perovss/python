import bs4
import re
import requests
from fake_headers import Headers
from decorator import logger
KEYWORDS = {'привет', 'фото', 'web', 'python', 'Сейчас', 'статья'}

URL = 'https://habr.com'
target_url = URL + '/ru/all/'
HEADER = Headers(
        # browser="chrome",  # Generate only Chrome UA
        # os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()
response = requests.get(target_url, headers=HEADER)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article" ,class_='tm-articles-list__item')
data_list ={}

@logger()
def find_article(text):
    result = str()
    for article in articles:
        for key in KEYWORDS:
            preview = article.find('div', class_='article-formatted-body').find(['p','div','br']).find(string=re.compile(key))
            if preview is not None:
                published = article.find('span', class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                links = article.find('a', class_='tm-article-snippet__title-link').attrs['href']
                header = article.find('a', class_='tm-article-snippet__title-link').find('span').contents[0]
                data_list['tag'] = key
                data_list['published'] = published
                data_list['links'] = URL + links
                data_list['header'] = header
                step = f"{data_list['published']} {data_list['header']} {data_list['links']}\n"
                result = result + step
    print(result)
    return result
if __name__ == '__main__':
    find_article("Аргумент")
