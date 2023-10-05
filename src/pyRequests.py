from bs4 import BeautifulSoup
import requests

class PyRequests:  
    def getSoupFromRequest(self, url: str):
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
        
        return BeautifulSoup(resp.content, 'html.parser')
