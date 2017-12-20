import urllib.request
import json
from .models import Sources, Articles

# Getting the API KEY
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources(source):
    """
    Function to retrieve news sources list from the News api
    """

    get_sources_url = base_url.format(source, api_key)
    #get_sources_url = 'https://newsapi.org/v1/sources'.format(source, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """Function that process the results list and transforms them into a list of objects
    Args: sources_list: A list of dictionaries that contains news sources details
    Returns:
    sources_results: a list of news sources objects"""

    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')

        source_object = Sources(id, name, description, url, category)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    '''
    Function to get a source and it's articles
    '''
    get_articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(article_list):
    '''
    Function that processes the article results and transform them to a list of objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []

    for article_item in article_list:
        source = article_item.get('source')
        title = article_item.get('title')
        urlToImage = article_item.get('urlToImage')
        description = article_item.get('description')
        urlToArticle = article_item.get('url')
        publishedAt = article_item.get('publishedAt')

        # if publishedAt != None:
        #     # Call publish_date_format method to convert date to a display-friendly format
        #     #date_to_display = article_item.publish_date_format(publishedAt) (self, author, title, description, urlToImage, url):
        article_object = Articles(source, title, description, urlToImage, urlToArticle, publishedAt)
        article_results.append(article_object)

    return article_results
