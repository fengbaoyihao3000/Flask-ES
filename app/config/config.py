#coding:utf-8
import os

DB_USERNAME = 'root'
DB_PASSWORD = None # 如果没有密码的话
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'flask_es'

class Config:
    SECRET_KEY ="hi" # 随机 SECRET_KEY
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True # 自动sql

    DEBUG = True # debug模式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%s:%s@%s:%s/%s' % (DB_USERNAME, DB_PASSWORD,DB_HOST, DB_PORT, DB_NAME) #数据库URL

    MAIL_SERVER = 'smtp.qq.com'
    MAIL_POST = 465
    MAIL_USERNAME = '3417947630@qq.com'
    MAIL_PASSWORD = '123456789'
    FLASK_MAIL_SUBJECT_PREFIX='M_KEPLER'
    FLASK_MAIL_SENDER=MAIL_USERNAME # 默认发送人
    # MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_DEBUG = False
    ENABLE_THREADS=True

