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


data1 = [
    {
        "name": "李雪",
        "img_url": "http://example.com/images/lixue.jpg",
        "article_count": 45,
        "followers_count": 987,
        "bio": "李雪是一位经验丰富的前端开发者，专注于现代 JavaScript 框架，如 React 和 Vue。她深入了解性能优化、响应式设计和移动端开发，致力于提升用户体验和开发效率。李雪是多本开发书籍的作者，并且她积极参与开源社区，贡献了许多实用的工具和插件。",
        "signature": "代码背后是创造的艺术，技术是实现梦想的桥梁。",
        "suggest": ["李雪", "前端开发", "React", "Vue", "性能优化", "开源贡献"],
        "weight": 1
    },
    {
        "name": "王磊",
        "img_url": "http://example.com/images/wanglei.jpg",
        "article_count": 102,
        "followers_count": 2035,
        "bio": "王磊是一位资深 JavaScript 开发者，专注于 Node.js 和全栈开发。多年来，他一直活跃在开发界，参与多个企业级项目的构建，并深入研究 JavaScript 的异步编程和性能调优。王磊也热衷于技术教育，经常在网络上发布 JavaScript 教程，并为开源社区贡献代码。",
        "signature": "用 JavaScript 改变世界，优化每一行代码。",
        "suggest": ["王磊", "全栈开发", "Node.js", "异步编程", "性能调优", "开源贡献"],
        "weight": 1
    },
    {
        "name": "赵丽",
        "img_url": "http://example.com/images/zhaoli.jpg",
        "article_count": 78,
        "followers_count": 1324,
        "bio": "赵丽是一位专注于 JavaScript 前端框架和自动化测试的开发者。她在公司里领导着多个跨平台应用的开发团队，并在许多技术博客上分享她的经验。赵丽还特别擅长结合 Jest 和 Mocha 等测试框架进行前端测试，以提高代码质量和开发效率。",
        "signature": "写出高质量的代码，打造可维护的产品。",
        "suggest": ["赵丽", "前端开发", "自动化测试", "Jest", "Mocha", "跨平台应用"],
        "weight": 1
    },
    {
        "name": "孙浩",
        "img_url": "http://example.com/images/sunhao.jpg",
        "article_count": 56,
        "followers_count": 1180,
        "bio": "孙浩是一位经验丰富的 JavaScript 开发者，专注于 Web 性能优化和 Progressive Web App（PWA）开发。他曾在多个大型项目中担任架构师，推动了公司从传统网页向现代化 Web 应用的转型。孙浩也积极参与前端技术的分享，致力于提升开发者对 Web 性能和用户体验的理解。",
        "signature": "为 Web 世界带来更流畅的体验和更高效的解决方案。",
        "suggest": ["孙浩", "Web 性能优化", "PWA", "前端架构", "用户体验", "技术分享"],
        "weight": 1
    }
]

data2 =[
    {
        "name": "算法游侠",
        "img_url": "http://example.com/images/algo_ranger.jpg",
        "article_count": 102,
        "followers_count": 2156,
        "bio": "算法游侠是一位信息检索领域的专家，致力于研究搜索引擎的深度优化和用户行为分析。他在 Lucene 和 Elasticsearch 框架下开发了多个高性能搜索系统，同时研究自然语言处理和语义检索模型。他的分享常聚焦于将理论与实践结合，为行业打造创新的解决方案。",
        "signature": "检索的深度是探索的高度。",
        "suggest": ["信息检索", "搜索优化", "Elasticsearch", "Lucene", "NLP", "语义搜索"],
        "weight": 2
    },
    {
        "name": "流数据巫师",
        "img_url": "http://example.com/images/data_wizard.jpg",
        "article_count": 78,
        "followers_count": 1893,
        "bio": "流数据巫师是一名大数据实时计算的爱好者，对 Kafka 和 Flink 流处理框架有深入的了解。他参与了多个实时大数据项目的架构设计和性能优化，通过高效的流数据处理管道帮助企业实现商业目标。此外，他还是流式数据分析领域的多场技术沙龙主讲人。",
        "signature": "掌控数据流，预见未来。",
        "suggest": ["流式处理", "Kafka", "Flink", "大数据架构", "实时计算"],
        "weight": 1
    },
    {
        "name": "小索引",
        "img_url": "http://example.com/images/index_fan.jpg",
        "article_count": 65,
        "followers_count": 1530,
        "bio": "小索引是索引技术和数据存储优化的爱好者，擅长设计高效的索引算法和数据结构。他曾参与多个企业搜索项目的设计和实现，特别在处理海量数据的分布式存储和索引优化方面积累了丰富经验。他热衷于分享技术心得，帮助开发者解决复杂的技术难题。",
        "signature": "让索引成为数据的指南针。",
        "suggest": ["索引优化", "分布式存储", "Elasticsearch", "信息检索", "海量数据"],
        "weight": 1
    },
    {
        "name": "云端玩家",
        "img_url": "http://example.com/images/cloud_master.jpg",
        "article_count": 88,
        "followers_count": 1720,
        "bio": "云端玩家专注于云计算和大数据平台的构建，是 Hadoop 和 Spark 技术的资深开发者。他在高并发、大规模分布式系统的设计中展现了非凡的能力，推动了企业云平台的建设。他主张“以架构应对复杂性”，多次在国内外技术大会上发表演讲。",
        "signature": "用云的视角俯瞰数据的海洋。",
        "suggest": ["云计算", "Hadoop", "Spark", "分布式系统", "高并发"],
        "weight": 2
    },
    {
        "name": "检索狂人",
        "img_url": "http://example.com/images/search_madman.jpg",
        "article_count": 92,
        "followers_count": 2048,
        "bio": "检索狂人专注于信息检索系统的开发与优化，擅长结合 AI 技术提升检索效果。他曾主导多个语义搜索项目，研究自然语言处理与向量化检索技术的结合，为企业提供创新的智能搜索解决方案。他对搜索引擎未来的发展方向充满激情，乐于分享知识。",
        "signature": "狂热于检索，执着于创新。",
        "suggest": ["语义搜索", "NLP", "智能检索", "向量化", "信息检索"],
        "weight": 1
    },
    {
        "name": "数据拾荒者",
        "img_url": "http://example.com/images/data_scout.jpg",
        "article_count": 81,
        "followers_count": 1637,
        "bio": "数据拾荒者擅长大数据分析与清洗，尤其在数据预处理和可视化方面有独到的见解。他曾主导多个涉及海量数据的项目，优化了从数据采集到清理的全流程。他倡导数据驱动决策，是行业内备受尊敬的“大数据工匠”。",
        "signature": "数据的每一片碎片，都有它的价值。",
        "suggest": ["数据清洗", "数据分析", "可视化", "大数据", "数据驱动"],
        "weight": 1
    }
]

data_ai =[
    {
        "name": "AI小白",
        "img_url": "http://example.com/images/ai_bai.jpg",
        "article_count": 72,
        "followers_count": 1345,
        "bio": "AI小白是一位致力于人工智能基础研究的开发者，特别对机器学习和深度学习有浓厚兴趣。他深入学习了 TensorFlow 和 PyTorch，开发了多个机器学习模型，并应用于自然语言处理和图像识别项目。AI小白也在多个技术社区活跃，经常分享人工智能的入门教程。",
        "signature": "人工智能，不止是技术，它是创造力的延伸。",
        "suggest": ["人工智能", "机器学习", "深度学习", "TensorFlow", "PyTorch", "NLP"],
        "weight": 2
    },
    {
        "name": "智能小鬼",
        "img_url": "http://example.com/images/smart_ghost.jpg",
        "article_count": 54,
        "followers_count": 1123,
        "bio": "智能小鬼是人工智能领域的新兴人才，专注于智能算法和机器人技术的研发。他参与过多个自动驾驶和智能硬件的项目，尤其擅长强化学习和计算机视觉技术。在他的指导下，团队成功将深度学习技术应用于图像处理和自动决策系统。",
        "signature": "用智能驱动未来，让机器思考。",
        "suggest": ["智能算法", "计算机视觉", "机器人", "深度学习", "自动驾驶"],
        "weight": 1
    },
    {
        "name": "数据怪兽",
        "img_url": "http://example.com/images/data_monster.jpg",
        "article_count": 83,
        "followers_count": 1689,
        "bio": "数据怪兽是一位经验丰富的人工智能工程师，专注于大数据分析和人工智能的结合应用。他通过开发高效的数据处理算法，成功帮助企业在海量数据中提取出有价值的信息，并利用机器学习模型进行智能预测。数据怪兽的技术博客已经成为数据科学爱好者的必看资源。",
        "signature": "数据的背后，是更大的世界。",
        "suggest": ["大数据", "机器学习", "人工智能", "智能预测", "数据处理"],
        "weight": 2
    },
    {
        "name": "脑洞大师",
        "img_url": "http://example.com/images/brain_masters.jpg",
        "article_count": 65,
        "followers_count": 2101,
        "bio": "脑洞大师是一位人工智能爱好者，他喜欢挑战人工智能的边界，探索最前沿的技术，尤其是在自然语言处理和人工智能推理方面。通过多年的研究，他掌握了深度神经网络、强化学习等技术，致力于让机器具有更高的智能。",
        "signature": "在人工智能的世界里，思维是无限的。",
        "suggest": ["自然语言处理", "深度神经网络", "强化学习", "智能推理", "人工智能前沿"],
        "weight": 1
    },
    {
        "name": "智链侠",
        "img_url": "http://example.com/images/smart_linker.jpg",
        "article_count": 96,
        "followers_count": 1789,
        "bio": "智链侠是一位致力于人工智能和区块链技术结合的开发者，专注于智能合约和去中心化应用。他的研究包括如何利用 AI 优化区块链的共识机制和智能合约的执行效率，为智能合约带来更高的自适应性和智能化。",
        "signature": "区块链与人工智能的融合，开启全新篇章。",
        "suggest": ["人工智能", "区块链", "智能合约", "去中心化", "AI优化"],
        "weight": 2
    },
    {
        "name": "算法大师",
        "img_url": "http://example.com/images/alg_master.jpg",
        "article_count": 120,
        "followers_count": 2203,
        "bio": "算法大师是一位在人工智能领域有深厚造诣的专家，他擅长设计高效的算法并将其应用于大规模机器学习和数据挖掘任务。他的研究涉及图像识别、语音识别和智能推荐等领域，通过算法创新推动了多项人工智能产品的突破。",
        "signature": "算法改变世界，智能引领未来。",
        "suggest": ["算法优化", "机器学习", "数据挖掘", "图像识别", "语音识别"],
        "weight": 1
    }
]


data_dj=[
    {
        "name": "Django小白",
        "img_url": "http://example.com/images/django_xiaobai.jpg",
        "article_count": 33,
        "followers_count": 789,
        "bio": "Django小白是一名热爱Web开发的开发者，专注于Django框架的学习和实践。他深入学习了Django的核心功能，包括ORM、路由、模板引擎等，致力于将Django应用于开发高效、可扩展的Web应用。他曾参与多个Django开源项目，并在社区中分享了大量实用的开发技巧和教程。",
        "signature": "用Django构建高效、稳定的Web应用。",
        "suggest": ["Django", "Web开发", "Python", "ORM", "Web框架", "开源贡献"],
        "weight": 1
    },
    {
        "name": "Django大师",
        "img_url": "http://example.com/images/django_master.jpg",
        "article_count": 58,
        "followers_count": 1452,
        "bio": "Django大师是一个在Django领域深耕多年的开发者，专注于Web应用的后端架构设计。他在多个复杂项目中应用Django框架，特别擅长性能优化、缓存机制的设计和Django REST Framework的使用。他在技术社区中有较高的知名度，提供了许多Django架构和开发的深度解析文章。",
        "signature": "架构决定应用的灵魂，Django赋予开发者无限可能。",
        "suggest": ["Django", "Web后端", "Django REST Framework", "性能优化", "架构设计", "Python"],
        "weight": 2
    },
    {
        "name": "Django飞狐",
        "img_url": "http://example.com/images/django_feihu.jpg",
        "article_count": 42,
        "followers_count": 1125,
        "bio": "Django飞狐是一名全栈开发者，专注于使用Django构建高效的Web后端系统，并且深入了解前端开发技术。飞狐的技术栈包括Django、JavaScript和数据库优化，致力于为用户提供流畅、高效的使用体验。他参与过多个知名开源项目，也积极与技术社区分享自己的开发经验和技巧。",
        "signature": "全栈开发，不止于前端与后端的结合。",
        "suggest": ["Django", "全栈开发", "数据库优化", "JavaScript", "开源项目", "Web应用"],
        "weight": 1
    },
    {
        "name": "Django小刀",
        "img_url": "http://example.com/images/django_xiaodao.jpg",
        "article_count": 65,
        "followers_count": 1589,
        "bio": "Django小刀是一名Web开发工程师，专注于基于Django的Web开发和数据驱动的应用系统。他特别擅长构建高效的API，并通过使用Django Rest Framework和GraphQL实现了多个大规模系统的后端接口。他的开发哲学是通过简洁的代码实现高效的系统，致力于提升开发团队的生产力。",
        "signature": "代码是一种优雅的艺术，Django是实现它的工具。",
        "suggest": ["Django", "Web开发", "Django Rest Framework", "GraphQL", "API设计", "Python"],
        "weight": 1
    },
    {
        "name": "Django女王",
        "img_url": "http://example.com/images/django_nvwang.jpg",
        "article_count": 49,
        "followers_count": 1340,
        "bio": "Django女王是一位全栈开发者，精通Django框架以及JavaScript、Vue.js等前端技术。她致力于使用Django实现高效的Web后端开发，尤其擅长设计可扩展的系统架构，并推动团队使用自动化测试和CI/CD提升开发效率。她的技术文章被多个技术社区转载，影响力日益增长。",
        "signature": "用Django的力量，打造不平凡的Web应用。",
        "suggest": ["Django", "全栈开发", "Vue.js", "JavaScript", "系统架构", "自动化测试"],
        "weight": 1
    }
]

data_vue=[
    {
        "name": "Vue小猴",
        "img_url": "http://example.com/images/vue_xiaohou.jpg",
        "article_count": 56,
        "followers_count": 1245,
        "bio": "Vue小猴是一位充满活力的前端开发者，专注于 Vue.js 生态系统的研究和实践。他深入学习了 Vue Router、Vuex 和 Vue 3 的新特性，喜欢使用 Vue.js 来构建动态、高效的用户界面。除了在开源社区发布技术文章，他还积极贡献 Vue 相关的插件和工具，帮助开发者提升开发效率。",
        "signature": "写代码不只是为了功能，还是为了优雅。",
        "suggest": ["Vue.js", "前端开发",  "Vue 3", "JavaScript"],
        "weight": 1
    },
    {
        "name": "Vue大神",
        "img_url": "http://example.com/images/vue_dashen.jpg",
        "article_count": 87,
        "followers_count": 2301,
        "bio": "Vue大神是一个资深的前端工程师，专注于使用 Vue.js 来构建复杂的单页面应用。他对 Vue 组件化开发有深入理解，并在多个大型项目中成功应用 Vue.js。Vue大神喜欢分享关于 Vue 性能优化和最佳实践的经验，他的文章经常成为开发者学习 Vue 的必读之作。",
        "signature": "技术的深度，来源于对细节的关注。",
        "suggest": [ "SPA", "Vue性能优化", "单页面应用", "JavaScript", "前端架构"],
        "weight": 2
    },
    {
        "name": "Vue大侠",
        "img_url": "http://example.com/images/vue_daxia.jpg",
        "article_count": 34,
        "followers_count": 872,
        "bio": "Vue大侠是一名 Vue.js 爱好者，致力于将 Vue 用于构建更快、更高效的应用。他的工作重点是 Vue 的状态管理和数据流控制，尤其喜欢使用 Vuex 结合 Vue.js 构建复杂应用的逻辑层。Vue大侠也经常参与 Vue 相关的社区活动，为开发者解答技术疑惑。",
        "signature": "每一行代码，都是向理想靠近的步伐。",
        "suggest": [ "Vuex", "状态管理", "前端开发", "Vue Router", "Web开发"],
        "weight": 1
    },
    {
        "name": "Vue萌妹",
        "img_url": "http://example.com/images/vue_mengmei.jpg",
        "article_count": 48,
        "followers_count": 1153,
        "bio": "Vue萌妹是一名充满热情的前端开发者，专注于 Vue.js 框架的前端开发。她特别喜欢使用 Vue.js 搭配各种前端工具和插件，以提高开发效率。Vue萌妹在学习过程中积累了大量关于 Vue 的实战经验，经常分享 Vue 中的细节处理和最佳实践，帮助新人快速入门。",
        "signature": "编写清晰、简洁的代码，是我永远的追求。",
        "suggest": [ "Vue开发", "前端优化", "Vue插件", "JavaScript", "开源贡献"],
        "weight": 1
    },
    {
        "name": "Vue狂人",
        "img_url": "http://example.com/images/vue_kuangren.jpg",
        "article_count": 72,
        "followers_count": 1567,
        "bio": "Vue狂人是一名对 Vue.js 框架痴迷的前端工程师，擅长将 Vue 应用到复杂的企业级项目中，特别是在大型数据展示和交互式应用的开发上有着丰富的经验。他对 Vue 的响应式数据流和生命周期有深刻理解，并擅长通过 Vue 进行组件复用和模块化开发。",
        "signature": "代码背后的乐趣，源于探索未知的可能。",
        "suggest": [ "前端开发", "组件化", "响应式设计", "Vue生态", "JavaScript"],
        "weight": 1
    }
]


# 向 Elasticsearch 插入数据
def insert_data():
    for author in data_vue:
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
                "name": {
                    "type": "text",
                    "analyzer": "ik_max_word"  # 使用 ik 分词器
                },
                "bio": {
                    "type": "text",
                    "analyzer": "ik_max_word"
                },
                "signature": {
                    "type": "text",
                    "analyzer": "ik_max_word"
                }
            }
        }
    }

    # 创建索引
    client.indices.create(index=index_name, body=mapping)
    print(f"索引 {index_name} 已创建。")


# 删除索引
def delete_index(index_name):
    if client.indices.exists(index=index_name):
        client.indices.delete(index=index_name)
        print(f"索引 {index_name} 已删除。")
    else:
        print(f"索引 {index_name} 不存在，无需删除。")


import requests
# Elasticsearch 服务器地址
ES_HOST = "http://localhost:9200"
INDEX_NAME = "authors"  # 索引名称

def test_suggest(prefix):
    """
    测试 Elasticsearch 的 suggest 功能
    :param prefix: 搜索前缀
    """
    url = f"{ES_HOST}/{INDEX_NAME}/_search"
    payload = {
        "suggest": {
            "author_suggest": {
                "prefix": prefix,
                "completion": {
                    "field": "suggest",
                    "fuzzy": {"fuzziness": 2},  # 允许2个编辑距离的模糊匹配
                    "size": 10  # 返回最多10条结果
                }
            }
        }
    }
    response = requests.post(url, json=payload)
    print("Suggest Response:")
    print(response.json())


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

# 执行数据插入
if __name__ == "__main__":
    insert_data()
    print("数据已成功插入到 Elasticsearch 中")

    # 设置您想要查询的索引名称
    #index_name = "authors"
    #fetch_all_data(index_name)

    # 删除索引
    #delete_index(index_name)
    # 创建新索引
    #create_index(index_name)

    # 调用函数删除文档
    # delete_document(doc_id, index_name)
    #response = delete_all_documents(index_name)
    #print(response)

    # 替换为你希望查询的前缀
    #test_suggest("J")