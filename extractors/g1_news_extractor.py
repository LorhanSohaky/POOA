import requests
from bs4 import BeautifulSoup

from news import News
from .abstract_news_extractor import AbstractNewsExtractor

class G1NewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://g1.globo.com')

    def extract_news(self):
        news = []
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')

        for item in soup.find_all('a', 'feed-post-link'):
            title = item.get_text()
            url = item.get('href')
            news.append(News(title,url))

        return news