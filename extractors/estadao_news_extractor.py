import requests
from bs4 import BeautifulSoup

from news import News
from .abstract_news_extractor import AbstractNewsExtractor


class EstadaoNewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://www.estadao.com.br')

    def extract_news(self):
        news = []
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        for item in soup.find_all('h3','title'):
            for item_filho in item.find_all('a'):
                title = item_filho.get('title')
                url = item_filho.get('href')
                news.append(News(title,url))

        return news