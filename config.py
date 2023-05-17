class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    #DEBUG = True
    SQLALCHEMY_ECHO = True
    
    ENV="development"
    SECRET_KEY = '9a36ceab2f1b06b936fd4ca4cd3f221e5a6158670486e5ffe124299054690a60'
    SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2023@localhost/dreamteam_db'
    
class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_ECHO = True
    
    ENV="production"

class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    ENV="testing"

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

"""
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
class ProductionConfig(Config):
    SECRET_KEY="98d0s809SD990AS)(dS&A&*d78(*&ASD08A"
    DATABASE_URI = 'mysql://user@localhost/foo'
class DevelopmentConfig(Config):
    ENV="development"
    SECRET_KEY="9as8df(*S*8(das0ˆSˆD%5a67900SA(D*00"
    DEBUG = True
class TestingConfig(Config):
    TESTING = True
"""