import scrapy
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

class GnosisSpider(scrapy.Spider):
    name = 'Mertz blurbs'
    start_urls = ['https://www.gnosis.cx/publish/']
    link_extractor = LinkExtractor()
    blurbs = set()
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        # Look for the potential "About"
        for h3 in soup.find_all('h3'):
            if h3.text.lower() == 'about the author':
                blurb = h3.find_next('p').text
                blurb = ' '.join(blurb.split())
                blurb = blurb.split("David may be reached at")[0]
                if blurb not in self.blurbs:
                    self.blurbs.add(blurb)
                    yield {'blurb': blurb}
                
        # Look for links either way
        for link in self.link_extractor.extract_links(response):
            if 'gnosis.cx/publish' not in link.url or '.htm' not in link.url:
                continue    # Only follow links under path
            yield response.follow(link, self.parse)
