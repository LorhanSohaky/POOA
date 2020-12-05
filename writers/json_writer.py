import json
from .abstract_writer import AbstractWriter

class JSONWriter(AbstractWriter):
    def __init__(self):
        pass
    
    def write_file(self,output_filename, list_news):
        json_list = []

        for news in list_news:
            json_list.append(news.__dict__)

        file = open(f'{output_filename}.json',mode='w')

        json.dump(json_list,file,indent=2)
        
        file.close()
