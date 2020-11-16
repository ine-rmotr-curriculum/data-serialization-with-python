import scrapy
from bs4 import BeautifulSoup

class QuotesSpider(scrapy.Spider):
    name = 'Quotes'
    start_urls = ['http://quotes.toscrape.com/']
    
    custom_settings = {
        "DEPTH_LIMIT": 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 0.25,
    }
    
    def parse(self, response):
        soup = BeautifulSoup(response.text)
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').string
            author = text.find_next(class_="author").text
            yield {'author': author,
                   'text': text.replace('“', '').replace('”', '')}
  
        next_page = soup.find('li', class_='next').find('a')['href']
        if next_page is not None:
            yield response.follow(next_page, self.parse)
