from bs4 import BeautifulSoup
import requests

class PyRequests:  
    def getSoupFromRequest(self, url: str):
        page = requests.get(url)
        if page.status_code != 200:
            return False
        
        return BeautifulSoup(page.content, 'html.parser')
        # except requests.exceptions.HTTPError as err:
        #     print(page.status_code)
        #     raise SystemExit(err)
