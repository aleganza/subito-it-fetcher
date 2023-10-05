from bs4 import BeautifulSoup
from urlBuilder import URLBuilder
from scraper import Scraper

urlBuilder = URLBuilder()
scraper = Scraper()

url = urlBuilder.buildUrl('iPhone 14 Pro', 'Ferrara', 'usato', False, True, False)
articles = scraper.getArticles(url)
print(articles)
