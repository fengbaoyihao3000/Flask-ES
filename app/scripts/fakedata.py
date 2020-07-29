#coding=utf-8
import time
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import requests
from pymongo import MongoClient
client = MongoClient(host="119.23.140.162",port=27017)
db = client['天眼查']
collection = '净水机'

datas = db.get_collection(collection).find({},{'_id':0,})

es = Elasticsearch("http://localhost:9200")
index = "tyc"
#create index
es.indices.create(index=index, ignore=400)
actions = []

def init():
  i = 0
  for data in datas:
    action = {
      "_index": index,
      "_type": "tyc_data",
      "_id": None,
      "_source": {
        "Name": data['企业名称'],
        "City": data['城市'],
        "Fa": data['法人代表'],
        "M": data['注册资金'],
        "Link": data['网址链接'],
        "createTime": data['成立时间'],
        "Status": data['状态'],
        "Desc": data['附加信息'],
        "Email": data['邮箱'],
        "Tel": data['联系电话']

      }
    }
    # print(action)
    actions.append(action)
    i += 1

    helpers.bulk(es, actions)

if __name__ == "__main__":
  init()