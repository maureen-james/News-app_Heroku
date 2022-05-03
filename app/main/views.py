# from flask import render_template
# import APP
# from ..requests import get_news, get_articles, process_results
# from models import Source, Article


# @APP.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data
#     '''
#     #Get the most popular news list
#     sports = get_news('sports')
#     technology = get_news('technology')
#     health = get_news('health')
#     business = get_news('business')
#     entertainment = get_news('entertainment')
#     print(technology)

#     title = 'DailyNews'
#     return render_template('index.html', title = title, sports = sports, technology = technology, health = health, business = business, entertainment = entertainment)

# @APP.route('/articles/<news_id>')
# def articles(news_id):
#     '''
#     A view function that will return the source of the article and its data
#     '''
#     articles = get_articles(news_id)
#     return render_template('articles.html', articles = articles)

from . import main
from flask import render_template,request,redirect,url_for,abort
from ..request import get_news, get_article,search_for_article,process_results


@main.route('/')
def index():
    # articles=get_article(source_id)
    articles=get_news('category')
    sports=get_news('sports')
    business=get_news('business')
    # sources=get_news()

    search=request.args.get('search_name')   

    if search:
        return redirect(url_for('.search',article_name=search))
    else:
         return render_template('index.html',article=articles,sports=sports,business=business)   

   

@main.route('/articles')
def articles():
    '''
    A view function that will return the source of the article and its data
    '''
    articles = get_article()
     
    
     #Make request to get article from server
    # search=request.args.get('search_name')   

    # if search:
    #     return redirect(url_for('.search',article_name=search))
    # else:
    return render_template('articles.html', articles = articles)    
    

@main.route('/search/<article_name>')
def search(article_name):
    artcle_name_list=article_name.split(" ")
    artcle_name_format="+".join(artcle_name_list)
    searched_article=search_for_article(artcle_name_format)
    title=f'{article_name}'

    return render_template('search.html',title=title,article=searched_article)