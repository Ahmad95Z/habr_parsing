from random import choice
from bs4 import BeautifulSoup as BS
import requests

url = 'https://habr.com/ru/all/'


headers = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
]
posts=[]

res = requests.get(url,headers=choice(headers))
    
if res.status_code == 200:
        soup = BS(res.content, 'html.parser')
        article =soup.find('article',class_='tm-articles-list__item')
        div = article.find_all_next('div',class_='tm-article-snippet')
        for i in div:
            title = i.find('h2',class_='tm-article-snippet__title tm-article-snippet__title_h2').text.strip()
            user = i.find('div',class_='tm-article-snippet__meta-container').text.strip()
            url = 'https://habr.com' + i.find('h2', class_ = 'tm-article-snippet__title tm-article-snippet__title_h2').a['href']
            profile =  'https://habr.com'  + i.a['href']
            image = i.find('img', class_='tm-article-snippet__lead-image').a['src']
            description = i.find('div', class_='article-formatted-body article-formatted-body_version-2').text
            views = i.find('div',class_='tm-icon-counter tm-data-icons__item')
            save = i.find('div',class_='bookmarks-button tm-data-icons__item')
            posts.append({'title':title,'user':user, url:url,'profile':profile,
                        'image':image,'views':views,'save':save,'description':description})
   
        