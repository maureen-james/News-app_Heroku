
import urllib.request,json
from .models import Source,Article
from datetime import datetime

# Getting api key
api_key = None

# Getting base urls
base_url=None
article_url=None
search_url=None


def configure_request(app):
    global api_key,base_url,article_url,search_url

    api_key = app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']
    article_url=app.config['NEWS_ARTICLE_BASE_URL']
    search_url=app.config['SEARCH_SOURCES']

def get_news(category):
    '''
    Function that gets the json response from our url request
    '''
    source_api_url='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'.format(category,api_key)

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
            new_source=Source( id, name, description, url,category, language, country)
            news_results.append(new_source)

    return news_results

def get_articles(id):

    article_url= 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(article_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        
        if article_details_response['articles']:
            article_results_list = article_details_response['articles']

        article_results = []
        if article_details_response["totalResults"] > 0:

            for article_item in article_results_list:
                name= article_item.get('source').get('name')
                author = article_item.get('author')
                title = article_item.get('title')
                urlToImage = article_item.get('urlToImage')
                description = article_item.get('description')
                url = article_item.get('url')
                publishedAt = article_item.get('publishedAt')
                
                publishedAt = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ').date()

                if urlToImage != "null":
                    article_object = Article(name,author,urlToImage,description,title,url,publishedAt)
                    article_results.append(article_object)
        else:
            return 
    return article_results


    

