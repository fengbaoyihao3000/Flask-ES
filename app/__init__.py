# coding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__,template_folder='templates',static_folder='static')
app.config.from_object(Config)

db = SQLAlchemy(app)
db.init_app(app)

csrf = CSRFProtect(app)
mail = Mail(app)
# 不要在生成db之前导入注册蓝图。
from app.home.baike import baike as baike_blueprint
from app.home.math import math as math_blueprint
from app.home.home import home as home_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(math_blueprint,url_prefix="/math")
app.register_blueprint(baike_blueprint,url_prefix="/baike")


