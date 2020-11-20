import scrapy
from bs4 import BeautifulSoup as BS

class PythonTitle(scrapy.Spider):
    name = 'Title of python.org'
    start_urls = ['https://www.python.org/']
    
    def parse(self, response):
        return {'title': BS(response.text).title.text}
