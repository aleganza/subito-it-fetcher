# Subito.it Searcher

```
url = urlBuilder.buildUrl('iPhone 14 Pro', 'Ferrara', 'usato', False, True, False)
articles = scraper.getArticles(url)
print(articles)
```

```
{
   "articlesNumber":25,
   "title":"IPhone 14 Pro a Ferrara e provincia",
   "pagesNumber":1,
   "articles":[
        {
            "link":"https://www.subito.it/telefonia/cover-iphone-14-pro-max-nuove-ferrara-514692557.htm",
            "title":"Cover iphone 14 pro max nuove",
            "place":"Ferrara ",
            "province":"FE",
            "date":"4 ott",
            "time":"17:06",
            "price":"10\\xa0€",
            "sold":false
        },
        ...
   ]
}
```