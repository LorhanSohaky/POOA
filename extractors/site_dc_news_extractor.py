import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from .abstract_news_extractor import AbstractNewsExtractor
from news import News

# Option to don't shows the browser
os.environ['MOZ_HEADLESS'] = '1'

class SiteDCNewsExtractor(AbstractNewsExtractor):
    def __init__(self):
        super().__init__('https://site.dc.ufscar.br/mais-noticias')

    def extract_news(self):
        news = []

        driver = webdriver.Firefox()
        driver.get(self.url)

        buttonMore = driver.find_element(By.XPATH, '//button[text()="Carregar mais"]')

        # Click while has more news
        while buttonMore.is_enabled():
            buttonMore.click()
            sleep(0.01)

        cards = driver.find_elements_by_xpath('//div[contains(@class,"card-body")]')
        for card in cards:
            url = card.find_element_by_tag_name('a').get_attribute('href')
            title = card.find_element_by_class_name('card-title').text
            news.append(News(title,url))


        driver.close()
        return news