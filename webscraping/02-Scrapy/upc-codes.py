import scrapy
from bs4 import BeautifulSoup

class UPCSpider(scrapy.Spider):
    name = 'UPC codes of all books'
    start_urls = ['http://books.toscrape.com/']
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        # First yield the UPC if it is a book page
        for tr in soup.find_all('tr'):
            if tr.th.text == 'UPC':
                yield {'UPC': tr.td.text, 'URL': response.url}
                break
                
        # Look for links either way
        for a in soup.find_all('a'):
            href = a['href']
            if href.startswith('http') and 'toscrape.com' not in href:
                # Only follow domain links
                continue
            yield response.follow(href, self.parse)
