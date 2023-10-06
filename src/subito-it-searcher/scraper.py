import json
from pyRequests import PyRequests

class Scraper:
    def __init__(self):
        self.pyReq = PyRequests()
        self.classNames = json.load(open('./assets/data/classNames.json'))
        
    def __getPageArticles(self, soup):
        return soup.find_all('div', {'class': self.classNames["pageArticles"]})
    
    def __getArticlesNumber(self, soup):
        return soup.find_all('p', {'class': self.classNames["articlesNumber"]})[0].text.split(' ')[0]
    
    def __getPageTitle(self, soup):
        return soup.find_all('h1', {'class': self.classNames["pageTitle"]})[0].text
    
    def __getArticlePageLink(self, article):
        return article.find_all('a', href = True)[0]['href']
    
    def __getArticleTitle(self, article):
        return article.find('h2', {'class': self.classNames["articleTitle"]}).text
    
    def __getArticlePlace(self, article):
        return (article.find('span', {'class': self.classNames["articlePlace"]}).text
                if not self.__isArticleSold(article)
                else "")
    
    def __getArticleProvince(self, article):
        return (article.find('span', {'class': self.classNames["articleProvince"]}).text.replace('(', '').replace(')', '')
                if not self.__isArticleSold(article)
                else "")
    
    def __getArticleDate(self, article):
        return (article.find('span', {'class': self.classNames["articleDate"]}).text.split(' alle ')[0]
                if not self.__isArticleSold(article)
                else '')
        
    def __getArticleTime(self, article):
        return (article.find('span', {'class': self.classNames["articleDate"]}).text.split(' alle ')[1]
                if not self.__isArticleSold(article)
                else '')
        
    def __getArticlePrice(self, article):
        return (article.find('p', {'class': self.classNames["soldArticlePrice"]}).text.replace('Venduto', '')
                if self.__isArticleSold(article)
                else article.find('p', {'class': self.classNames["articlePrice"]}).text.replace('Spedizione disponibile', ''))
                        
    def __isArticleSold(self, article):
        return (True
            if article.find('p', {'class': self.classNames["soldArticlePrice"]})
            else False)
        
    def __isPageNotEmpty(self, soup):
        return (True
                if soup.find_all('div', {'class': self.classNames["pageArticles"]})
                else False)

    def getArticles(self, url):
        page = 1
        parsedUrl = url + f'&o=1'
        soup = self.pyReq.getSoupFromRequest(parsedUrl)
        
        if not self.__isPageNotEmpty(soup):
            return {}
        
        articlesObject = {
            "articlesNumber": int(self.__getArticlesNumber(soup)),
            "title": self.__getPageTitle(soup),
            "pagesNumber": '',
            "articles": []
        }
        
        while self.__isPageNotEmpty(soup):
            articles = self.__getPageArticles(soup)
            
            # TODO: add vetrina key
            for div in articles:
                articlesObject["articles"].append(
                    {
                        "link": self.__getArticlePageLink(div),
                        "title": self.__getArticleTitle(div),
                        "place": self.__getArticlePlace(div),
                        "province": self.__getArticleProvince(div),
                        "date": self.__getArticleDate(div),
                        "time": self.__getArticleTime(div),
                        "price": self.__getArticlePrice(div),
                        "sold": self.__isArticleSold(div)
                    }
                )
            
            page += 1
            parsedUrl = url + f'&o={page}'
            soup = self.pyReq.getSoupFromRequest(parsedUrl)
            
        articlesObject["pagesNumber"] = page-1
            
        return articlesObject
                