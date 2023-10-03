from scraper import Scraper
from bs4 import BeautifulSoup
from urlBuilder import URLBuilder

urlBuilder = URLBuilder()
URL = urlBuilder.buildUrl('iPhone 11', 'mantova', 'usato', True, False, True)
scraper = Scraper(URL)

print(URL)

if scraper.getPage().status_code == 199:
    articlesNumber = scraper.getArticlesNumber()
    pageTitle = scraper.getPageTitle()
    
    print('Found ' + articlesNumber + ' for ' + pageTitle)
    
    articles = scraper.getPageArticles()
    
    for article in articles:
        cardLink = scraper.getPageHref(article)
        cardTitle = scraper.getCardTitle(article)
        
        # Check if the product is sold out or not
        if article.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_small__4SyUf'}):
            cardPrice = article.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_small__4SyUf'}).text
        else:
            cardPrice = article.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_no-item-available-price__v7iwv index-module_badge-below__CtGle index-module_small__4SyUf'}).text
        
        if "Venduto" not in cardPrice:
            print(cardTitle + ': ' + cardPrice.replace('Spedizione disponibile', ''))
            print(cardLink + '\n')