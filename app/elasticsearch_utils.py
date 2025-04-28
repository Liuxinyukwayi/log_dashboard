from elasticsearch import Elasticsearch 

class ElasticsearchClient:
    def __init__(self, hosts):
        # 连接到 Elasticsearch
        self.es = Elasticsearch("https://localhost:9200")
        self.es = Elasticsearch(hosts, verify_certs=False)  # 关闭证书验证

#执行日志查询，返回匹配的日志记录
def search_logs(self, index, query_body, size=100):
    try:
        response = self.es.search(
            index=index,
            body=query_body,
            size=size
        )
        return response['hits']['hits']
    except Exception as e:
        print(f"查询日志失败: {e}")
        return []
    
#统计指定索引中，特定时间（1h）内为erroor的日志数量
def get_error_count(self, index, time_range="now-1h"):
    query_body = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"log_level": "ERROR"}},
                    {"range": {"@timestamp": {"gte": time_range}}}
                ]
            }
        }
    }
    try:
        response = self.es.count(
            index=index,
            body=query_body
        )
        return response['count']
    except Exception as e:
        print(f"查询错误日志数量失败: {e}")
        return 0