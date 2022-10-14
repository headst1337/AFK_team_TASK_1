import os

class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'YOUR_RANDOM_SECRET_KEY'


class ProductionConfig(Config):
    DEBUG = False
    SERVER_NAME = '0.0.0.0:3000'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVER_NAME = '127.0.0.1:3000'