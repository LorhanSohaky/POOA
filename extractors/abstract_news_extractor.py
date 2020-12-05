from abc import ABC, abstractmethod

class AbstractNewsExtractor(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def extract_news(self):
        raise NotImplementedError()
