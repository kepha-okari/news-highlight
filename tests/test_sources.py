import unittest
# from app import app
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test class to test behaviours of the Sources class

    Args:
        unittest.TestCase : Test case class that helps create test cases
    '''

    def setUp(self):
        """ Set up method to run before each test case """
        self.news_source = Sources('abc-news-au','ABC News (AU)', 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.',"http://www.abc.net.au/news","general")

    def test_instance(self):
        '''
        Test case to check if self.news_source is an instance of Source
        '''
        self.assertTrue( isinstance( self.news_source, Sources ) )

    def test_init(self):
        '''
        Test case to check if the Source class is initialised
        '''
        self.assertEqual( self.news_source.id, 'abc-news-au')
        self.assertEqual( self.news_source.name, 'ABC News (AU)')
        self.assertEqual( self.news_source.description, 'Australia\'s most trusted source of local, national and world news. Comprehensive, independent, in-depth analysis, the latest business, sport, weather and more.')

if __name__ == '__main__':
    unittest.main(verbosity=2)
