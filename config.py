import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'iamsosecret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELEOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
        'production': ProductionConfig,
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'staging': StagingConfig
        }
