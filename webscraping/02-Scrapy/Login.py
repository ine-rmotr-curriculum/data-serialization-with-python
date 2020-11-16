import scrapy
from bs4 import BeautifulSoup
from random import random, choice

def authentication_failed(response):
    # Check the contents of the response, True if failed
    soup = BeautifulSoup(response.text, 'lxml')
    has_logout = [a for a in soup.find_all('a') if a.text == 'Logout']
    # randomly fail sometimes
    return not has_logout or random() > 0.75

class LoginSpider(scrapy.Spider):
    name = 'Login quotes.toscrape.com'
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        login_link = [a['href'] for a in soup.find_all('a') 
                                if a.text == 'Login'][0]
        return response.follow(login_link, self.login)

    def login(self, response):
        self.user = choice(['user1', 'user2', 'user3', 'user4'])
        return scrapy.FormRequest.from_response(
            response, callback=self.after_login, 
            formdata={'username': self.user, 'password': 'pw'})

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error(f"Login failed for {self.user}")
            return 
        # Get one random quote author
        return response.follow('/random', self.author)
          
    def author(self, response):
        for quote in response.css('div.quote'):
            yield {'author': quote.xpath('span/small/text()').get()}