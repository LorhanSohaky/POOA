import xml.etree.ElementTree as ET

from .abstract_writer import AbstractWriter

class XMLWriter(AbstractWriter):
    def __init__(self):
        pass
    
    def write_file(self,output_filename, list_news):
        file = open(f'{output_filename}.xml',mode='w')

        file.write(f'<items>\n')
        for news in list_news:
            file.write(f'\t<item>\n')
            file.write(f'\t\t<title>{news.title}</title>\n')
            file.write(f'\t\t<url>{news.url}</url>\n')
            file.write(f'\t</item>\n')
        file.write(f'</items>')
        
        file.close()
