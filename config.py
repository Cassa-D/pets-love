from environs import Env
from os import environ
from secrets import token_hex

env = Env()
env.read_env()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    JWT_SECRET_KEY = token_hex(16)
    SECRET_KEY = token_hex(16)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env('SQLALCHEMY_DATABASE_URI')
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = environ.get('POSTGRES_URI')
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    SECRET_KEY = environ.get('SECRET_KEY')
