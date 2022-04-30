import os

class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')