from bs4 import BeautifulSoup
from urlBuilder import URLBuilder
from scraper import Scraper

urlBuilder = URLBuilder()
scraper = Scraper()

url = urlBuilder.buildUrl('iPhone', 'ferrara', 'usato', True, False, True)

articles = scraper.getArticles(url)

print(articles)
