# Subito.it Web Scraper

```
url = urlBuilder.buildUrl('iPhone 14 Pro', 'Ferrara', 'usato', False, True, False)
articles = scraper.getArticles(url)
print(articles)
```

```
{
   "articlesNumber": 25,
   "title": "IPhone 14 Pro a Ferrara e provincia",
   "pagesNumber": 1,
   "articles": [
        {
            "link": "https://www.subito.it/telefonia/cover-iphone-14-pro-max-nuove-ferrara-514692557.htm",
            "title": "Cover iphone 14 pro max nuove",
            "price": "10\\xa0€",
            "sold": false
        },
        {
            "link": "https://www.subito.it/telefonia/iphone-14-pro-max-256-giga-nuovo-ferrara-514691544.htm",
            "title": "IPHONE 14 PRO MAX 256 GIGA NUOVO",
            "price": "1.100\\xa0€",
            "sold": false
        },
        ...
   ]
}
```