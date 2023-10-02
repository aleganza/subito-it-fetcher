from scraper import Scraper
from bs4 import BeautifulSoup
import json

def parsePlace(place):
    return place.replace(' ', '-').replace('\'', '-').lower()

def buildUrl(query: str, place: str, category: str, municipalityOnly: bool, shippingOnly: bool, titleOnly: bool):
    domain = 'https://www.subito.it/'
    
    place = place.replace(' ', '-').replace('\'', '-').lower()
    
    # create regions array
    regions = []
    
    for regionName in json.load(open('./assets/data/italyRegions.json')):
        regions.append(regionName["nome"].replace(' ', '-').replace('\'', '-').lower())
    
    province = ''
    
    if place not in regions:
        # create places array
        places = json.load(open('./assets/data/italyProvinces.json'))
        
        ''' for placeInfo in json.load(open('./assets/data/italyProvinces.json')):
            places.append({"name": placeInfo["nome"].replace(' ', '-').replace('\'', '-').lower(), 
                           "region": placeInfo["regione"].replace(' ', '-').replace('\'', '-').lower()}) '''
        
        if place not in places[0].values():
            raise ValueError(f'Region ({place} is not a valid argument!)')
        else:
            province = place + '/'
            place = 'we'
    
    
    # TODO: usato should be a category
    return (f'{domain}annunci-{place}/vendita/usato/{province}')
    

URL = 'https://www.subito.it/annunci-emilia-romagna/vendita/usato/ferrara/ferrara/?q=iPhone%2011'

scraper = Scraper(URL)

print(buildUrl('iPhone 11', 'milano', 'moto', 3, 4, 5))

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
