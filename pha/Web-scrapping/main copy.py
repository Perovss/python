import bs4
import requests
from fake_headers import Headers
HUBS1 = ['Visual Basic for Applications','CSS','Настройка Linux']
# URL1 = 'https://2ip.ru'
URL2 = 'https://habr.com'
target_url = URL2 + '/ru/all/'
HEADER = Headers(
        # browser="chrome",  # Generate only Chrome UA
        # os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    ).generate()
# response = requests.get(URL1)
# text = response.text

# soup = bs4.BeautifulSoup(text, features='html.parser')

# ip_address1 = soup.find(id='d_clip_button').find('span')
response = requests.get(target_url, headers=HEADER)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all("article")
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hub_list = [hub.find('span').text for hub in hubs]
    # for hub in hubs:
    #     hubq = hub.find('span').text
    #     hub1.append(hubq)
    for hub in hub_list:
        if hub in HUBS1:
            title = article.find('h2').find('span').text
            link = article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
            result = f'Статья -> {title} / {URL2 + link}'
            print(result)