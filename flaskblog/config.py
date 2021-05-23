import os

import pymysql


class Config:
    SECRET_KEY = 'iyFasUFoigTGsdVY'
    SQLALCHEMY_DATABASE_URI = '''mysql+pymysql://be2fac96f093e6:b99da497@us-cdb\
r-east-03.cleardb.com/heroku_48739ce63cdccc0'''
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'projeto.t4ss0@gmail.com'
    MAIL_PASSWORD = 'T4SS0gmail2021'
    SCHEDULER_API_ENABLED = True

