# -*- coding:utf-8 -*-
from flask import Blueprint

baike = Blueprint("baike", __name__)

from app.home.baike import views

