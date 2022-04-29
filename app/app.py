from flask import render_template
from app import app
from .requests import get_news, get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)

@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)  

def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title)



@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting top headlines
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best news Review Website Online'
    return render_template('index.html', title = title,popular = popular_news) 

# @app.route('/')
# def index():

    # '''
    # View root page function that returns the index page and its data
    # '''

    # # Getting popular movie
    # popular_movies = get_movies('popular')
    # upcoming_movie = get_movies('upcoming')
    # now_showing_movie = get_movies('now_playing')
    # title = 'Home - Welcome to The best Movie Review Website Online'
    # return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )