import scrapy
from scrapy.linkextractors import LinkExtractor

class PG_NewTitles(scrapy.Spider):
    # A snapshot of the current "new titles" on Project Gutenberg
    name = 'New Titles'
    link_extractor = LinkExtractor()
    start_urls = ['https://dev.gutenberg.org/browse/recent/last1.html.utf8']
    
    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            # Many links to general navigation, a heuristic to narrow results
            if 'ebooks' in link.url:
                yield {"title": link.text, "url": link.url}
                # This would recurse into linked pages. Not permitted by PG
                # yield Request(link.url, callback=self.parse)
