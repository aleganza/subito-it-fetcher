import requests
from bs4 import BeautifulSoup
import json

class Scraper:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.classNames = json.load(open('./assets/data/classNames.json'))
        
    def getUrl(self):
        return self.url
    
    def getPage(self):
        return self.page
    
    def getArticlesNumber(self):
        return self.soup.find_all('p', {'class': self.classNames["articlesNumber"]})[0].text
    
    def getPageTitle(self):
        return self.soup.find_all('h1', {'class': self.classNames["pageTitle"]})[0].text

    def getPageArticles(self):
        return self.soup.find_all('div', {'class': self.classNames["pageArticles"]})
    
    def getPageHref(self, article):
        return article.find_all('a', href = True)[0]['href']
    
    def getCardTitle(self, article):
        return article.find('h2', {'class': self.classNames["cardTitle"]}).text

    