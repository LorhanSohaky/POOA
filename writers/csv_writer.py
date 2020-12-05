from abc import ABC, abstractmethod

class CSVWriter(ABC):
    def __init__(self, output_filename):
        self.output_filename = output_filename

    @abstractmethod
    def write_file(self):
        raise NotImplementedError()
