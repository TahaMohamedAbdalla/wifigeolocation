import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/aruba"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/aruba"



class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI = "mongodb://localhost:27017/aruba"


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

GOOGLE_KEY = 'AIzaSyCCK6hPzvUI1_XbDCV4pC1HN_6bneUejYc'





