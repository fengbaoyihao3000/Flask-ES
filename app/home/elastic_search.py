from elasticsearch import Elasticsearch

es = Elasticsearch()


def search(query,count: int = 15):
    dsl = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "content", "tag"]
            }
        },
        "highlight": {
            "fields": {
                "title": {}
            }
        }
    }
    match_data = es.search(index="spider", body=dsl, size=count)
    return match_data