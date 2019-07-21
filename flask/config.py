import os

class Config(object):
    base = 'mysql://'
    user = "ikarus2k"
    password = "bottest123"
    host = "db"
    database = "bot"

    #base = 'mysql+pymysql://root:@'

    SQLALCHEMY_DATABASE_URI = base + user + ':' + password + '@' + host + '/' + database
    SQLALCHEMY_TRACK_MODIFICATIONS = False