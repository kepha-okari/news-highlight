import os


class Config:
    """Main configurations class"""

    NEWS_API_KEY = 'd3f684e44cfa412aa3f3f932571b5618'
    NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/'
    #NEWS_API_BASE_URL = 'https://newsapi.org/v1/sources/{}?apiKey={}' // APPLIES WHEN THE base_url is passes as the string



class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    pass


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
