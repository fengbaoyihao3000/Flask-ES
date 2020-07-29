
import json
from datetime import datetime
import pymongo
from app.elasticsearchClass import elasticSearch

client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['spider']
sheet = db.get_collection('Spider').find({}, {'_id': 0, })

es = elasticSearch(index_type="spider_data",index_name="spider")
es.create_index()

for i in sheet:
    data = {
            'title': i["title"],
            'content':i["data"],
            'link': i["link"],
            'create_time':datetime.now()
        }

    es.insert_one(doc=data)






# dsl = {
#     "query": {
#         "multi_match": {
#             "query": "爬虫",
#             "fields": ["title", "tag"]
#         }
#     },
#     "highlight": {
#         "fields": {
#             "name": {}
#         }
#     }
# }
#
# result = es.search()
# print(json.dumps(result, indent=2, ensure_ascii=False))





  

