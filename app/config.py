import os

class config:
    """
    Class that contains the configuration for the app
    """

    NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey={194f9337ee204d7990dd869f9cddc6c3}"
    NEWS_API_KEY = os.environ.get('194f9337ee204d7990dd869f9cddc6c3')

class ProdConfig(config):

    """
    Production  configuration child class
    """
    pass

class DevConfig(config):
    """
    Development  configuration child class
    """

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


