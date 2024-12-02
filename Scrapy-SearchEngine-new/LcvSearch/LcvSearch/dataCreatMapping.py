from elasticsearch import Elasticsearch
from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer,  Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

# 连接到 Elasticsearch 服务
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# 定义索引名称
index_name = 'jobbole'


def create_mapping():
    # 检查索引是否存在
    if es.indices.exists(index=index_name):
        try:
            # 添加新的字段映射（completion 类型）到现有索引
            mapping_body = {
                "properties": {
                    "suggest": {
                        "type": "completion",
                        "analyzer": "ik_max_word",
                        "preserve_separators": True,
                        "preserve_position_increments": True,
                        "max_input_length": 50
                    }
                }
            }

            # 更新索引映射
            response = es.indices.put_mapping(index=index_name, body=mapping_body)
            print(f"映射更新成功: {response}")
        except Exception as e:
            print(f"更新映射时出错: {e}")
    else:
        print(f"索引 '{index_name}' 不存在。")


if __name__ == "__main__":
    create_mapping()
