import os

#coneccon a bd con orm
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'Clave_nueva'
    SESSION_COOKIE_SECURE = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://maria:maria@127.0.0.1/prueba'
    SQLALCHEMY_TRACK_MODIFICATIONS = False