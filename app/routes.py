# app/routes.py

from flask import Blueprint, render_template, request, jsonify
from . import es_client

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    return render_template('dashboard.html')

@main.route('/api/search', methods=['POST'])
def search_logs():
    keyword = request.json.get('keyword', '')
    index = request.json.get('index', 'filebeat-*')

    query_body = {
        "query": {
            "multi_match": {
                "query": keyword,
                "fields": ["message", "log_level", "host.name"]
            }
        },
        "sort": [
            {"@timestamp": {"order": "desc"}}
        ]
    }

    results = es_client.search_logs(index=index, query_body=query_body)
    return jsonify(results)

@main.route('/api/error_count', methods=['GET'])
def error_count():
    index = request.args.get('index', 'filebeat-*')
    time_range = request.args.get('time_range', 'now-1h')

    count = es_client.get_error_count(index=index, time_range=time_range)
    return jsonify({"error_count": count})
