class Source:
    '''
    Define the News Sources object
    '''

    def __init__(self, id, name, description, url, category, language, country):
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

    def __init__(self,author,title,description,url,image,publishedate,content):
        self.author = author
        self.title =title 
        self.description = description
        self.url = url
        self.image= image
        self.publishedate= publishedate
        self.content= content

