from scraper import Scraper
from bs4 import BeautifulSoup
import json

PROVINCES_JSON = json.load(open('./assets/data/italyProvinces.json'))
REGIONS_JSON = json.load(open('./assets/data/italyRegions.json'))

def parsePlace(place):
    return place.replace(' ', '-').replace('\'', '-').lower()

def getProvinces():
    return [parsePlace(d["nome"]) for d in PROVINCES_JSON if "nome" in d]

# TODO: do parsePlace of PROVINCES_JSON
def getProvincesFromRegion(region):
    return [parsePlace(d["nome"]) for d in PROVINCES_JSON if d["regione"] == region]


def buildUrl(query: str, place: str, category: str, municipalityOnly: bool, shippingOnly: bool, titleOnly: bool):
    domain = 'https://www.subito.it/'
    
    place = parsePlace(place) # get formatted version of place argument
        
    if place not in getProvinces(): # if argument place is a region
        raise ValueError(f'Place argument ({place}) is not a valid argument!')
    else:
        print("è una provincia")
    
    # TODO: usato should be a category
    return (f'{domain}annunci-{place}/vendita/usato/')
    

URL = 'https://www.subito.it/annunci-emilia-romagna/vendita/usato/ferrara/ferrara/?q=iPhone%2011'

scraper = Scraper(URL)

print(buildUrl('iPhone 11', 'Milano', 'moto', 3, 4, 5))

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
