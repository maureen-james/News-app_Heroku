import unittest
from app.models import Article
class TestArticle(unittest.TestCase):
    def setUp(self):
        self.new_article=Article('by maureen','CNN','killer cat','www.cnn.com','from','skjsdjfkd.jpg','12/12/15','killer',)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article)) 

    
         
