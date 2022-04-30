import app
import urllib.request,json
from .models import Source, Article


# Getting api key
api_key = None
# Getting the news base url
base_url = None
# Getting the articles url
articlesurl = None


def config_request(app):
    global api_key, base_url, articlesurl
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articlesurl = app.config['NEWS_ARTICLES_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name=news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')


        if url:
            news_object = Source(id,name, description, url, category, language, country)
            news_results.append(news_object)


    return news_results

def get_articles(news_id):
    '''
    Get json response of the requested url
    '''
    # Insert the articles url manually by replacing "url"
    get_articles_url = 'url'.format(news_id,api_key) 

    with urllib.request.urlopen(get_articles_url, data=None) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_list = None

        if get_articles_response['articles']:
            articles_list_results = get_articles_response['articles']
            articles_list = process_articles[articles_list_results]
    return articles_list

def process_articles(articles_list):
    '''
    A function that will process the articles result and transform them to a list of objects
    '''
    articles_results = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        publishedate = article_item.get('publishedAt')
        image = article_item.get('urlToImage')

        if publishedate and author and image:
            article_object = Article(author, title, description, url, image, publishedate)
            articles_results.append(article_object)
    
    return articles_results