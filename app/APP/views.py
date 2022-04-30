from flask import render_template
import APP
from ..requests import get_news, get_articles, process_results
from ..models import Source, Article


@APP.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    #Get the most popular news list
    sports = get_news('sports')
    technology = get_news('technology')
    health = get_news('health')
    business = get_news('business')
    entertainment = get_news('entertainment')
    print(technology)

    title = 'DailyNews'
    return render_template('index.html', title = title, sports = sports, technology = technology, health = health, business = business, entertainment = entertainment)

@APP.route('/articles/<news_id>')
def articles(news_id):
    '''
    A view function that will return the source of the article and its data
    '''
    articles = get_articles(news_id)
    return render_template('articles.html', articles = articles)