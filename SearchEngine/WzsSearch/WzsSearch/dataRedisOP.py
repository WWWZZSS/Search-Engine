import redis

# 连接到 Redis 服务
redis_cli = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

# 插入数据到 Redis
def insert_data_to_redis():
    # 假设 jobbole_count 是一个整型值，表示某些记录的条数
    jobbole_count = 100  # 示例数据
    redis_cli.set("jobbole_count", jobbole_count)
    print(f"Data inserted: jobbole_count = {jobbole_count}")

# 查询 Redis 中的数据
def get_data_from_redis():
    jobbole_count = redis_cli.get("jobbole_count")
    if jobbole_count:
        print(f"Fetched data: jobbole_count = {jobbole_count}")
    else:
        print("Data not found in Redis.")



def insert_data_hash():
    article_count = {
        '知乎': 891,
        'CSDN': 342,
        '百度': 189,
        '博客园': 456,
        '掘金': 673,
        '百度开发者搜索': 200,
        'Goobe': 547,
        '腾讯云': 872,
        'Hacker': 239,
        'Stack': 230,
        'GitHub': 690,
        'DuckDuckGo': 76,
    }

    # 使用 hset 存储每个字段（逐个存储每个键值对）
    for key, value in article_count.items():
        redis_cli.hset("article_count", key, value)

def get_data_hash():
    # 从 Redis 哈希中读取所有字段
    article_count = redis_cli.hgetall("article_count")  # 返回字典，键和值都是字符串
    print(article_count)
    print(article_count.get('知乎'))

def delete_data_hash():
    # 使用 hdel 删除 article_count 哈希表中的所有数据
    redis_cli.hdel("article_count", *redis_cli.hkeys("article_count"))  # 删除所有键
    print("已删除 article_count 中的所有数据")


# 主程序
if __name__ == "__main__":
    # 插入数据
    #insert_data_to_redis()

    # 查询数据
    #get_data_from_redis()

    insert_data_hash()
    #delete_data_hash()

    get_data_hash()
