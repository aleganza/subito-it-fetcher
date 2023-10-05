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

    def getArticles(self, url, nPages):
        articlesObject = {
            "articlesNumber": 0,
            "title": '',
            "articles": []
        }
        
        articlesNumber = 0
        
        for page in range(1, nPages):
            if not self.pyReq.getSoupFromRequest(url + f'&o={page}') == False:
                break
            
            soup = self.pyReq.getSoupFromRequest(url + f'&o={page}')
            
            articlesHTML = self.__getPageArticlesHTML(soup)
            pageTitle = self.__getPageTitle(soup)
            
            articlesObject['title'] = pageTitle
            articlesNumber += int(self.__getArticlesNumber(soup).split(' ')[0]);
            
            for div in articlesHTML:
                article = {
                    "link": self.__getArticlePageLink(div),
                    "title": self.__getArticleTitle(div),
                    "price": (
                        div.find('p', {'class': self.classNames["soldArticlePrice"]}).text.replace('Venduto', '')
                        if self.__isArticleSold(div)
                        else div.find('p', {'class': self.classNames["articlePrice"]}).text.replace('Spedizione disponibile', '')),
                    "sold": self.__isArticleSold(div)
                }
                articlesObject["articles"].append(article)
                
        articlesObject["articlesNumber"] = articlesNumber
                
        return articlesObject
                