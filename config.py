# -*- coding:utf-8 -*-
import os
class Config:
    SECRET_KEY = (os.getenv('SECRET_KEY') or 'hard to guess string')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 30
    POSTS_AUTH_PAGE = 150
    UPLOAD_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/uploads/')
    USER_UPLOAD_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app/static/uploads/users/')
    WECHAT_TOKEN = (os.getenv('WECHAT_TOKEN') or 'wechat_token')
    WECHAT_APPID = (os.getenv('WECHAT_APPID') or 'wechat_appid')
    WECHAT_APPSECRET = (os.getenv('WECHAT_APPSECRET') or 'wechat_appsecret')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dev:6Jn,+nHpZnUr[AFX@localhost:3306/db_cs_meeting'
    REDIS_URL = 'redis://:password@106.14.124.91:6379/0'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    REDIS_URL =''

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (os.getenv('DB_URI') or 'db_uri')
    REDIS_URL = (os.getenv('REDIS_URL') or 'redis_url')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}