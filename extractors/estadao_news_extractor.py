import requests
from bs4 import BeautifulSoup

from .abstract_news_extractor import AbstractNewsExtractor
from news import News

class EstadaoNewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://www.estadao.com.br')

    def extract_news(self):
        news = []
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        for item in soup.find_all('h3','title'):
            for abacaxi in item.find_all('a'):
                title = abacaxi.get('title')
                url = abacaxi.get('href')
                news.append(News(title,url))

        return news