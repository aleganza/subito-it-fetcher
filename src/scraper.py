from urllib.parse import urlparse, parse_qs, urlencode
from bs4 import BeautifulSoup
import json
from pyRequests import PyRequests

class Scraper:
    def __init__(self):
        self.pyReq = PyRequests()
        self.classNames = json.load(open('./assets/data/classNames.json'))
        
    def __getPageArticlesHTML(self, soup):
        return soup.find_all('div', {'class': self.classNames["pageArticles"]})
    
    def __getArticlesNumber(self, soup):
        return soup.find_all('p', {'class': self.classNames["articlesNumber"]})[0].text
    
    def __getArticlePageLink(self, article):
        return article.find_all('a', href = True)[0]['href']
    
    def __getArticleTitle(self, article):
        return article.find('h2', {'class': self.classNames["articleTitle"]}).text
    
    def __getPageTitle(self, soup):
        return soup.find_all('h1', {'class': self.classNames["pageTitle"]})[0].text
    
    def __isArticleSold(self, articleHTML):
        return (True
            if articleHTML.find('p', {'class': self.classNames["soldArticlePrice"]})
            else False)
        
    def __isPageNotEmpty(self, soup):
        return (True
                if soup.find_all('div', {'class': self.classNames["pageArticles"]})
                else False)

    def getArticles(self, url):
        page = 1
        parsedUrl = url + f'&o=1'
        soup = self.pyReq.getSoupFromRequest(parsedUrl)
        
        articlesObject = {
            "articlesNumber": int(self.__getArticlesNumber(soup).split(' ')[0]),
            "title": self.__getPageTitle(soup),
            "pagesNumber": '',
            "articles": []
        }
        
        while self.__isPageNotEmpty(soup):
            articlesHTML = self.__getPageArticlesHTML(soup)
            
            for div in articlesHTML:
                articlesObject["articles"].append(
                    {
                        "link": self.__getArticlePageLink(div),
                        "title": self.__getArticleTitle(div),
                        "price": (
                            div.find('p', {'class': self.classNames["soldArticlePrice"]}).text.replace('Venduto', '')
                            if self.__isArticleSold(div)
                            else div.find('p', {'class': self.classNames["articlePrice"]}).text.replace('Spedizione disponibile', '')),
                        "sold": self.__isArticleSold(div)
                    }
                )
            
            page += 1
            parsedUrl = url + f'&o={page}'
            soup = self.pyReq.getSoupFromRequest(parsedUrl)
            
        articlesObject["pagesNumber"] = page-1
            
        return articlesObject
                