from . import main
from flask import render_template
from ..request import get_news, get_articles


@main.route('/')
def index():

    sports=get_news('sports')
    business=get_news('business')
    entertainment=get_news('entertainment')
    health=get_news('health')
    technology=get_news('technology')
    science=get_news('science')
    general=get_news('general')
    

    
    return render_template('index.html',sports=sports,business=business,entertainment=entertainment,health=health,technology=technology,science=science,general=general)   

@main.route('/sports/')
def sports():
    sports=get_news('sports')
    
    return render_template('sports.html',sports=sports)

@main.route('/business/')
def business():
    business=get_news('business')
    
    return render_template('business.html',business=business)




@main.route('/article/')
def articles():
    '''
    A view function that will return the source of the article and its data
    '''
    # articles = get_article('articles')
    # sports=get_news('sports')
    # business=get_news('business')
    article = get_articles('article')

    if article:
        for i in article:
            name = i.name
    else:
         name = ""
    print (article)    
    
    return render_template('article.html',article=article,name=name)
    
