import requests
from bs4 import BeautifulSoup

URL = 'https://www.subito.it/annunci-emilia-romagna/vendita/usato/ferrara/ferrara/?q=iPhone%2011'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

if page.status_code:
    num_results_div = soup.find_all('p', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-caption__TaQWv size-normal index-module_weight-semibold__MWtJJ total-ads AdsCount_total-ads__9aTXA'})[0].text
    title_div = soup.find_all('h1', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ'})[0].text
    
    print('Found ' + num_results_div + ' for ' + title_div)
    
    card_divs = soup.find_all('div', {'class': 'items__item item-card item-card--small'})
    
    for i in card_divs:
        cardLink = i.find_all('a', href=True)[0]['href']
        cardTitle = i.find('h2', {'class': 'index-module_sbt-text-atom__ed5J9 index-module_token-h6__FGmXw size-normal index-module_weight-semibold__MWtJJ ItemTitle-module_item-title__VuKDo SmallCard-module_item-title__1y5U3'}).text
        
        # Check if the product is sold or not
        if i.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_small__4SyUf'}):
            cardPrice = i.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_small__4SyUf'}).text
        else:
            cardPrice = i.find('p', {'class': 'index-module_price__N7M2x SmallCard-module_price__yERv7 index-module_no-item-available-price__v7iwv index-module_badge-below__CtGle index-module_small__4SyUf'}).text
        
        if "Venduto" not in cardPrice:
            print(cardTitle + ': ' + cardPrice.replace('Spedizione disponibile', ''))
            print(cardLink + '\n')

    