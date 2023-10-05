from bs4 import BeautifulSoup
from urlBuilder import URLBuilder
from scraper import Scraper

urlBuilder = URLBuilder()
scraper = Scraper()

url = urlBuilder.buildUrl('iPhone 11', 'mantova', 'usato', True, False, True)

nPages = 4
articles = scraper.getArticles(url, nPages)

print(articles)
