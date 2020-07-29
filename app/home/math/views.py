# -*- coding:utf-8 -*-
import os

from flask_paginate import Pagination, get_page_parameter
from app.Logger.logger import log_v
from app.elasticsearchClass import  elasticSearch
from app.home.forms import SearchForm

from app.home.math import math
from flask import request, render_template, redirect

math_es = elasticSearch(index_type="math_data",index_name="math")



@math.route("/")
def index():
    searchForm = SearchForm()
    return render_template('math/index.html', searchForm=searchForm)

@math.route("/search", methods=['GET', 'POST'])
def mathSearch():
    search_key = request.args.get("m", default=None)
    if search_key:
        searchForm = SearchForm()
        log_v.error("[+] Search Keyword: " + search_key)
        match_data = math_es.search(search_key,count=30)

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
            'uid_link': "/math/"
        }
        return render_template('data.html', q=search_key, searchForm=searchForm, **context)
    return redirect('home.index')



@math.route('/<uid>')
def mathSd(uid):
    base_path = os.path.abspath('app/templates/s_d/')
    old_file = os.listdir(base_path)[0]
    old_path = os.path.join(base_path, old_file)
    file_path = os.path.abspath('app/templates/s_d/{}.html'.format(uid))
    if not os.path.exists(file_path):
        log_v.debug("[-] File does not exist, renaming !!!")
        os.rename(old_path, file_path)
    match_data = math_es.get_doc(uid=uid)
    return render_template('s_d/{}.html'.format(uid), match_data=match_data)

