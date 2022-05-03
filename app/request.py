import urllib.request,json
from .models import Source,Article
from . import request

# Getting api key
api_key = None

# Getting base urls
base_url=None
article_url=None
search_url=None


def configure_request(app):
    global api_key,base_url,article_url,search_url

    api_key = '044e110d04e84886a4057da519c842af'
    base_url=app.config['NEWS_API_BASE_URL']
    article_url=app.config['NEWS_ARTICLE_BASE_URL']
    search_url=app.config['SEARCH_SOURCES']

def get_news(category):
    '''
    Function that gets the json response from our url request
    '''
    source_api_url=base_url.format(category,api_key)

    with urllib.request.urlopen(source_api_url) as url:
        unread_data=url.read()
        read_json=json.loads(unread_data)

        news_results=None

        if read_json['sources']:
            news_list=read_json['sources']
            news_results=process_results(news_list)

    return news_results

def process_results(news_list):
    '''
    Function  that processes the sources result and transforms them to a list of Objects
    '''
    news_results = []
    for news in news_list:
        id=news.get('id')
        name=news.get('name')
        description=news.get('description')
        url=news.get('url')
        category=news.get('category')
        country=news.get('country')
        language=news.get('language')
        
        if description:
            new_source=Source(id,name,description,url,category,country,language)
            news_results.append(new_source)

    return news_results

def get_article():
    get_articles_url= 'https://newsapi.org/v2/everything?sources={}apiKey={}'.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_data=url.read()
        get_json_data=json.loads(get_data)

        articles_data=None

        if get_json_data['articles']:
            articles_list=get_json_data['articles']
            articles_data=process_article(articles_list)
        
    return articles_data

def process_article(articles_data):
    '''
    Function  that processes the sources result and transform them to a list of Objects according to objects
    '''
    articles_list=[]

    for article in articles_data:
        id=article.get('id')
        author=article.get('author')
        urlToImage=article.get('urlToImage')
        description=article.get('description')
        publishedAt=article.get('publishedAt')
        url=article.get('url')
        title=article.get('title')
        source=article.get('source')
        if publishedAt and author and urlToImage:
            new_article=Article(id,author,urlToImage,description,title,url,publishedAt,source)
            articles_list.append(new_article)

    return articles_list

def search_for_article(article):
    search_article_url= 'https://newsapi.org/v2/everything?q={}&apiKey=044e110d04e84886a4057da519c842af'.format(article,api_key)

    with urllib.request.urlopen(search_article_url) as url:
        search_data=url.read()
        search_json=json.loads(search_data)

        search_article=None

        if search_json['articles']:
            searches=search_json['articles']
            search_article=process_article(searches)

    return search_article