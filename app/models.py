class Source:
    '''
    Define the News Sources object
    '''

    def __init__(self, id, name, description, url,category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
        

class Article:
    '''
    News Article class to define News Article Objects
    '''

    def __init__(self,id,author,urlToImage,description,title,url,publishedAt,source):
        self.id = id
        self.author = author
        self.urlToImage=urlToImage
        self.description = description
        self.title =title 
        self.url = url
        self.source = source
        self.publishedAt= publishedAt
        self.source= source

