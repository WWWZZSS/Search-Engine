from elasticsearch import Elasticsearch


def delete_document(doc_id, index_name):
    try:
        client = Elasticsearch(hosts=["localhost"])  # 创建连接 Elasticsearch 客户端
        # 删除文档
        response = client.delete(index=index_name, id=doc_id)
        print(f"Successfully deleted document with _id: {doc_id}")
        print(response)  # 打印删除操作的响应
    except Exception as e:
        print(f"Error occurred while deleting the document: {e}")

def delete_all_documents(index_name):
    # 连接到本地 Elasticsearch 服务
    es = Elasticsearch(["http://localhost:9200"])

    # 删除索引中的所有数据，但保留索引结构
    response = es.delete_by_query(
        index=index_name,
        body={
            "query": {
                "match_all": {}
            }
        }
    )

    return response


if __name__ == "__main__":
    # 要删除的文档 ID 和索引名称
    doc_id = '1'
    index_name = 'jobbole'

    # 调用函数删除文档
    # delete_document(doc_id, index_name)
    response = delete_all_documents(index_name)
    print(response)

