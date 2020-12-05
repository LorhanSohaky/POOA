from abc import ABC, abstractmethod

class AbstractWriter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def write_file(self,output_filename, list_news):
        raise NotImplementedError()
