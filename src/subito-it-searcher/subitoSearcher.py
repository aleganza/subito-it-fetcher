from urlBuilder import URLBuilder
from scraper import Scraper

class SubitoSearcher():
    def __init__(self):
        self.urlBuilder = URLBuilder()
        self.scraper = Scraper()
        
    def searchArticles(self, query: str, place: str, category: str = 'usato', municipalityOnly: bool = False, titleOnly: bool = False, shippingOnly: bool = False):
        return self.scraper.getArticles(
                                self.urlBuilder.buildUrl(query, place, category, municipalityOnly, titleOnly, shippingOnly)
                            )
