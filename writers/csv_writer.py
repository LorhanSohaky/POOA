import csv
from .abstract_writer import AbstractWriter

class CSVWriter(AbstractWriter):
    def __init__(self):
        pass
    
    def write_file(self,output_filename, list_news):
        file = open(f'{output_filename}.csv',mode='w')

        fields_name = ['title', 'url']
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fields_name)

        writer.writeheader()
        
        for news in list_news:
            writer.writerow(news.__dict__)
        
        file.close()
