import unittest
from models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Article class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_article = Articles('the-next-web','PlayStation\'s $30 PS4 gamepad for kids is totally adorable', 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/PS4-Mini-gamepad-social.jpg', 'Sony\'s teamed up with Hori on its new $30 Mini Wired Gamepad, which is designed for younger PS4 players with smaller hands.', 'https://thenextweb.com/gaming/2017/10/19/playstations-30-ps4-gamepad-for-kids-is-totally-adorable/', '2017-10-19T13:00:00Z')

    def test_instance(self):
        '''
        Test case to check if self.new_article is an instance of Article
        '''
        self.assertTrue( isinstance( self.new_article, Articles ) )

    def test_init(self):
        '''
        Test case to check if the Article class is initialised
        '''
        self.assertEqual( self.new_article.author, 'the-next-web')
        self.assertEqual( self.new_article.title, 'PlayStation\'s $30 PS4 gamepad for kids is totally adorable')
        self.assertEqual( self.new_article.urlToImage, 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/PS4-Mini-gamepad-social.jpg')
        self.assertEqual( self.new_article.description, 'Sony\'s teamed up with Hori on its new $30 Mini Wired Gamepad, which is designed for younger PS4 players with smaller hands.')
        self.assertEqual( self.new_article.urlToArticle, 'https://thenextweb.com/gaming/2017/10/19/playstations-30-ps4-gamepad-for-kids-is-totally-adorable/')
        self.assertEqual( self.new_article.publishedAt, '2017-10-19T13:00:00Z')

    def test_publish_date_format(self):
        '''
        Test case to check if UTC date format is converted to a display-friendly format
        '''
        display_friendly_format = self.new_article.publish_date_format(self.new_article.publishedAt)
        self.assertEqual( display_friendly_format, '2017-10-19')




if __name__ == '__main__':
    unittest.main(verbosity=2)
