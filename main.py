import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(this, url):
        this.url = url
        this.page = requests.get(url)
        this.soup = BeautifulSoup(this.page.content, 'html.parser')
        
    def getUrl(this):
        return this.url
    
    def getPage(this):
        return this.page
    
    def getArticlesNumber(this):
        return this.soup.find_all('p', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-caption__TaQWv size-normal index-module_weight-semibold__MWtJJ total-ads AdsCount_total-ads__9aTXA'})[0].text
    
    def getPageTitle(this):
        return this.soup.find_all('h1', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ'})[0].text

    def getPageArticles(this):
        return this.soup.find_all('div', {'class': 'items__item item-card item-card--small'})
    
    def getPageHref(this, article):
        return article.find_all('a', href=True)[0]['href']
    
    def getCardTitle(this, article):
        return article.find('h2', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ ItemTitle-module_item-title__VuKDo SmallCard-module_item-title__1y5U3'}).text

URL = 'https://www.subito.it/annunci-emilia-romagna/vendita/usato/ferrara/ferrara/?q=iPhone%2011'

scraper = Scraper(URL)
print(scraper.getUrl())

if scraper.getPage().status_code:
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
          
