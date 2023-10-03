import json
import urllib.parse

class URLBuilder:
    def __init__(self):
        self.PROVINCES_JSON = json.load(open('./assets/data/italyProvinces.json'))
        self.REGIONS_JSON = json.load(open('./assets/data/italyRegions.json'))

    def __parsePlace(self, place: str):
        return place.replace(' ', '-').replace('\'', '-').lower()

    def __getProvinces(self):
        return [self.__parsePlace(d["nome"]) for d in self.PROVINCES_JSON if "nome" in d]

    def __getRegions(self):
        return [self.__parsePlace(d) for d in self.REGIONS_JSON]

    def __getProvincesFromRegion(self, region: str):
        return [self.__parsePlace(d["nome"]) for d in self.PROVINCES_JSON if self.__parsePlace(d["regione"]) == self.__parsePlace(region)]

    def __getRegionFromProvince(self, province: str):
        return [self.__parsePlace(d["regione"]) for d in self.PROVINCES_JSON if self.__parsePlace(d["nome"]) == self.__parsePlace(province)][0]


    def buildUrl(self, query: str, place: str, category: str = 'usato', municipalityOnly: bool = False, titleOnly: bool = False, shippingOnly: bool = False):
        domain = 'https://www.subito.it/'
        
        place = self.__parsePlace(place)
        query = urllib.parse.quote_plus(query)
        municipality = ''
        province = ''
        title = '&qso=true' if titleOnly else ''
        shipping = '&shp=true' if shippingOnly else ''
            
        if place in self.__getProvinces():
            if municipalityOnly:
                municipality = '/' + place
            
            province = place
            region = self.__getRegionFromProvince(place)   
        elif place in self.__getRegions():
            if municipalityOnly:
                raise ValueError(f'municipalityOnly argument cannot be True if place is not a province!')
            
            region = place
        else:
            raise ValueError(f'Place argument ({place}) is not a valid argument!')
            
        
        return (f'{domain}annunci-{region}/vendita/{category}/{province}{municipality}/?q={query}{title}{shipping}')
            