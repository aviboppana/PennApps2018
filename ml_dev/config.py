class Config(object):
    test = False


class DevelopmentConfig(Config):
    DB_HOST = 'ds249942.mlab.com'
    DB_PORT = 49942
    DB_NAME = 'pennapps'

    DB_USER = 'hamoor'
    DB_PASS = 'H@ri1999'
    
    test = True


class ProductionConfig(Config):
    DB_HOST = 'ds249942.mlab.com'
    DB_PORT = 49942
    DB_NAME = 'pennapps'

    DB_USER = 'hamoor'
    DB_PASS = 'H@ri1999'
    
    test = True

