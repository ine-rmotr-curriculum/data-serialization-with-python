import scrapy

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
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            yield {'author': quote.xpath('span/small/text()').get(),
                   'text': text.replace('“', '').replace('”', '')}
  
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
