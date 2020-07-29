# -*- coding:utf-8 -*-
import os

import requests
from flask_paginate import Pagination, get_page_parameter
from app.Logger.logger import log_v
from app.elasticsearchClass import elasticSearch
from app.home.forms import SearchForm

from app.home.home import home
from flask import request, jsonify, render_template, redirect, Response, stream_with_context, send_from_directory

baike_es = elasticSearch(index_type="baike_data",index_name="baike")


@home.route("/")
def index():
    searchForm = SearchForm()
    return render_template('index.html', searchForm=searchForm)

@home.route("/search", methods=['GET', 'POST'])
def search():
    search_key = request.args.get("search_key", default=None)
    if search_key:
        searchForm = SearchForm()
        log_v.error("[+] Search Keyword: " + search_key)
        match_data = baike_es.search(search_key,count=30)

        # 翻页
        PER_PAGE = 10
        page = request.args.get(get_page_parameter(), type=int, default=1)
        start = (page - 1) * PER_PAGE
        end = start + PER_PAGE
        total = 30
        print("最大数据总量:", total)
        pagination = Pagination(page=page, start=start, end=end, total=total)
        context = {
            'match_data': match_data["hits"]["hits"][start:end],
            'pagination': pagination,
            'uid_link': "/baike/"
        }
        return render_template('data.html', q=search_key, searchForm=searchForm, **context)
    return redirect('home.index')


@home.route("/add", methods=['GET', 'POST'])
def refresh_posts():
    return jsonify({"success": 1, "message": "All Indexes Refreshed", "data": {}})


@home.errorhandler(400)
def page_not_found(error):
    return "400错误", 400


@home.errorhandler(500)
def page_not_found(error):
    return "500错误", 500
