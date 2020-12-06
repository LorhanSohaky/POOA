import requests
from bs4 import BeautifulSoup

from news import News
from .abstract_news_extractor import AbstractNewsExtractor


class FolhaNewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://www.folha.uol.com.br')

    def extract_news(self):
        news = []
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        for item in soup.find_all('ul','c-tools-share__list'):
            title = item.get('data-sharebar-text')
            url = item.get('data-sharebar-url')
            news.append(News(title,url))


        return news