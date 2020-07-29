# -*- coding:utf-8 -*-
from flask import Blueprint
math = Blueprint("math", __name__)

from app.home.math import views
