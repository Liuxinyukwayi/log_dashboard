# app/__init__.py

from flask import Flask
from .elasticsearch_utils import ElasticsearchClient

es_client = None  # 全局 Elasticsearch 客户端

def create_app():
    app = Flask(__name__)

    # 载入配置
    app.config.from_pyfile('../config.py', silent=True)

    # 初始化 Elasticsearch
    global es_client
    es_client = ElasticsearchClient(hosts=["http://localhost:9200"])  # 你的 Elasticsearch 地址

    # 注册蓝图或路由
    from .routes import main
    app.register_blueprint(main)

    return app
