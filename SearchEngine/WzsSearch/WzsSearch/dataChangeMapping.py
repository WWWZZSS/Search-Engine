from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import connections, Document, Text, Completion

# 连接到 Elasticsearch
es = Elasticsearch(hosts=["http://localhost:9200"])
index_name = "jobbole"

# 删除索引
def delete_index(index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"索引 {index_name} 已删除。")
    else:
        print(f"索引 {index_name} 不存在，无需删除。")

# 创建新索引和映射
def create_index(index_name):
    # 定义映射
    mapping = {
        "mappings": {
            "properties": {
                "suggest": {
                    "type": "completion",
                    "analyzer": "ik_max_word",  # 使用 ik 分词器
                    "preserve_separators": True,
                    "preserve_position_increments": True,
                    "max_input_length": 50
                },
                "title": {
                    "type": "text",
                    "analyzer": "ik_max_word"  # 使用 ik 分词器
                },
                "tags": {
                    "type": "text",
                    "analyzer": "ik_max_word"
                },
                "content": {
                    "type": "text",
                    "analyzer": "ik_max_word"
                }
            }
        }
    }

    # 创建索引
    es.indices.create(index=index_name, body=mapping)
    print(f"索引 {index_name} 已创建。")

# 主程序
if __name__ == "__main__":
    # 删除现有索引
    delete_index(index_name)

    # 创建新索引
    create_index(index_name)
