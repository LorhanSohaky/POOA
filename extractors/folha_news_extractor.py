import requests
from bs4 import BeautifulSoup

from .abstract_news_extractor import AbstractNewsExtractor
from news import News

class FolhaNewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://www.folha.uol.com.br')

    def extract_news(self):
        news = []
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        for item in soup.find_all('a','c-main-headline__url'):
            url = item.get('href')
            for abacaxi in item.find_all('h2','c-main-headline__title'):
                title = abacaxi.get_text()
            news.append(News(title,url))

        for item in soup.find_all('a','c-list-links__url'):
            url = item.get('href')
            for abacaxi in item.find_all('h2'):
                title = abacaxi.get_text()
                news.append(News(title,url))

        for item in soup.find_all('ul','c-tools-share__list'):
            title = item.get('data-sharebar-text')
            url = item.get('data-sharebar-url')
            news.append(News(title,url))

        return news