from elasticsearch import Elasticsearch

# 创建 Elasticsearch 客户端连接
client = Elasticsearch("http://localhost:9200")

def fetch_all_data(index_name):
    # 第一次查询，获取第一个批次数据
    response = client.search(
        index=index_name,
        body={
            "query": {
                "match_all": {}
            },
            "size": 1000  # 每次查询返回1000条数据
        },
        scroll="1m"  # scroll上下文有效时间
    )

    # 获取 scroll_id，后续查询将使用此 id
    scroll_id = response["_scroll_id"]

    # 打印第一页的数据
    print("Initial batch of data:")
    for hit in response["hits"]["hits"]:
        print(hit["_source"])

    # 获取后续批次的数据
    while True:
        # 调用 scroll API 获取后续的批次
        response = client.scroll(scroll_id=scroll_id, scroll="1m")

        # 如果没有更多的数据，退出循环
        if len(response["hits"]["hits"]) == 0:
            print("No more data.")
            break

        # 打印每批次返回的数据
        print("\nNext batch of data:")
        for hit in response["hits"]["hits"]:
            print(hit["_source"])

        # 更新 scroll_id，继续获取后续批次
        scroll_id = response["_scroll_id"]

if __name__ == "__main__":
    # 设置您想要查询的索引名称
    index_name = "jobbole"
    fetch_all_data(index_name)

