from bs4 import BeautifulSoup
from urlBuilder import URLBuilder
from scraper import Scraper

urlBuilder = URLBuilder()
scraper = Scraper()



url = urlBuilder.buildUrl('iPhone 14 Pro', 'Bologna', 'usato', False, True, False)
print(url)
articles = scraper.getArticles(url)
print(articles)
