from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from datetime import datetime
from models import AuthorType  # 引用之前定义的 ArticleType 类


# 建立连接
connections.create_connection(hosts=["localhost"])

# 创建 Elasticsearch 客户端
client = Elasticsearch(hosts=["127.0.0.1"])

data = [
    {
      "name": "张涛",
      "img_url": "http://example.com/images/zhangtao.jpg",
      "article_count": 83,
      "followers_count": 1520,
      "bio": "张涛是一位资深的前端开发工程师，专注于前端框架和JavaScript的深度应用。他不仅参与多个知名开源项目，还主导了多个前端技术的创新实践。他擅长技术分享，曾多次在技术大会上发表演讲，并带领团队将复杂的UI界面转化为高效可维护的代码。张涛的编程哲学是追求简洁与高效，致力于为开发者提供更好的技术解决方案。",
      "signature": "让技术与创意碰撞，编写美丽而高效的代码！",
      "suggest": ["张涛", "前端开发", "JavaScript", "技术创新", "开源贡献", "编程"],
      "weight": 1
    },

]

# 向 Elasticsearch 插入数据
def insert_data():
    for author in data:
        article_doc = AuthorType(
            name=author["name"],
            img_url=author["img_url"],
            article_count=author["article_count"],
            followers_count=author["followers_count"],
            bio=author["bio"],
            signature=author["signature"],
            suggest={
                "input": author.get("suggest", []),  # 自定义值
                "weight": author.get("weight", 1)
            }
        )
        article_doc.save(index="authors")   # 保存到 Elasticsearch



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


# 执行数据插入
if __name__ == "__main__":
    #insert_data()
    print("数据已成功插入到 Elasticsearch 中")

    # 设置您想要查询的索引名称
    index_name = "authors"
    fetch_all_data(index_name)
