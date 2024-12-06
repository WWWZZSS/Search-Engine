
import json  # 将返回的内容转为json数据使用
from django.shortcuts import render
from django.views.generic.base import View  # 用以SearchSuggest继承
from .models import ArticleType  # SearchSuggest里会使用
from .models import AuthorType  # SearchSuggest里会使用
from django.http import HttpResponse  # SearchSuggest中return使用，将数据返回给前端
from elasticsearch import Elasticsearch  # SearchView使用，建立es的连接；比es_dsl更底层的操作接口
from datetime import datetime  # 处理查询时间
import redis  # 处理搜索条数等


client = Elasticsearch(hosts=["127.0.0.1"])  # SearchView使用
redis_cli = redis.StrictRedis()  # 建立redis的连接



# Create your views here.
# 搜索建议
class SearchSuggest(View):
    def get(self, request):
        key_words = request.GET.get('s', '')
        s_type = request.GET.get('s_type', 'default')  # 获取搜索类型，默认值为 'default'
        print("SearchSuggest内部，s_type:", s_type)  # 打印 s_type 的值
        re_datas = []
        if key_words:
            if s_type == 'article':  # 如果搜索类型是文章
                print("1")
                s = ArticleType.search(index="jobbole")  # 查询 ArticleType 索引
            elif s_type == 'author':  # 如果搜索类型是书籍
                s = AuthorType.search(index="authors")  # 查询 AuthorType 索引
                print("2")
            else:  # 默认搜索
                s = ArticleType.search(index="jobbole")  # 默认使用 ArticleType 索引
                print("3")
            s = s.suggest('my_suggest', key_words, completion={  # s.suggest()：用于构建一个建议查询，定义搜索建议的方式和配置。
                "field": "suggest", "fuzzy": {
                    "fuzziness": 2
                },  # fuzziness为编辑距离
                "size": 10,
            })
            suggestions = s.execute()  # s.execute_suggest()：用于执行 s.suggest() 所构建的查询，并返回 Elasticsearch 的建议结果。
            # 从 Elasticsearch 返回的建议结果中提取每个匹配项的标题，并将其存储到 re_datas 列表中
            # for match in suggestions.my_suggest[0].options:
            #     source = match._source
            #     re_datas.append(source["title"])
            # 解析 suggestions 结果
            if "suggest" in suggestions and "my_suggest" in suggestions.suggest:
                count = 0  # 初始化计数器
                for match in suggestions.suggest['my_suggest'][0].options:
                    print(f"Match Option:  {count + 1}:{match}")  # 打印每个匹配项的详细内容
                    source = match.text  # 从 `text` 提取匹配数据
                    re_datas.append(source)

        # 将数据返回到前端中
        return HttpResponse(json.dumps(re_datas), content_type="application/json")



class SearchView(View):
    def get(self, request):
        key_words = request.GET.get("q", "")
        page = request.GET.get("p", "1")
        s_type = request.GET.get('s_type', 'default')  # 获取搜索类型，默认值为 'default'
        print("Search内部，s_type:", s_type)  # 打印 s_type 的值
        try:
            page = int(page)
        except:
            page = 1

        # jobbole_count = redis_cli.get("jobbole_count") #获取redis中记录条数数据
        # jobbole_count = redis_cli.get("jobbole_count")
        article_count = redis_cli.hgetall("article_count")  # 返回字典，键和值都是字符串
        # 将字节类型转换为字符串
        article_count = {key.decode(): value.decode() for key, value in article_count.items()}
        #print(article_count)
        # 如果从 Redis 获取到数据，转换为整数
        # if jobbole_count:
        #     jobbole_count = int(jobbole_count)  # 转换为整数类型
        # else:
        #     jobbole_count = 0  # 如果没有值，返回0

        start_time = datetime.now()
        # response = client.search(
        #     index="jobbole",
        #     body={
        #         "query": {
        #             "multi_match": {
        #                 "query": key_words,
        #                 "fields": ["tags", "title", "content"]
        #             }
        #         },
        #         "from": (page - 1) * 10,
        #         "size": 10,
        #         "highlight": {
        #             "pre_tags": ['<span class="keyWord">'],
        #             "post_tags": ['</span>'],
        #             "fields": {
        #                 "title": {},
        #                 "content": {},
        #             }
        #         }
        #     }
        # )
        if s_type == "article":
            print("search进入article")
            # 查询 ArticleType 索引
            response = client.search(
                index="jobbole",
                body={
                    "query": {
                        "multi_match": {
                            "query": key_words,
                            "fields": ["tags", "title", "content"]
                        }
                    },
                    "from": (page - 1) * 10,
                    "size": 10,
                    "highlight": {
                        "pre_tags": ['<span class="keyWord">'],
                        "post_tags": ['</span>'],
                        "fields": {
                            "title": {},
                            "content": {},
                        }
                    }
                }
            )
        elif s_type == "author":
            print("search进入author")
            # 查询 AuthorType 索引
            response = client.search(
                index="authors",
                body={
                    "query": {
                        "multi_match": {
                            "query": key_words,
                            "fields": ["name", "bio", "signature"]
                        }
                    },
                    "from": (page - 1) * 10,
                    "size": 10,
                    "highlight": {
                        "pre_tags": ['<span class="keyWord">'],
                        "post_tags": ['</span>'],
                        "fields": {
                            "name": {},
                            "bio": {},
                            "signature": {},
                        }
                    }
                }
            )
        else:
            # 默认查询 ArticleType
            response = client.search(
                index="jobbole",
                body={
                    "query": {
                        "multi_match": {
                            "query": key_words,
                            "fields": ["tags", "title", "content"]
                        }
                    },
                    "from": (page - 1) * 10,
                    "size": 10,
                    "highlight": {
                        "pre_tags": ['<span class="keyWord">'],
                        "post_tags": ['</span>'],
                        "fields": {
                            "title": {},
                            "content": {},
                        }
                    }
                }
            )

        end_time = datetime.now()
        last_seconds = (end_time - start_time).total_seconds()
        total_nums = response["hits"]["total"]["value"]  # 搜索到的所有数量
        if (page % 10) > 0:
            page_nums = int(total_nums / 10) + 1
        else:
            page_nums = int(total_nums / 10)
        hit_list = []
        for hit in response["hits"]["hits"]:
            hit_dict = {}
            # if "title" in hit["highlight"]:
            #     hit_dict["title"] = "".join(hit["highlight"]["title"])
            # else:
            #     hit_dict["title"] = hit["_source"]["title"]
            # if "content" in hit["highlight"]:
            #     hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]  # 只显示500个字
            # else:
            #     hit_dict["content"] = hit["_source"]["content"][:500]
            #
            # hit_dict["create_date"] = hit["_source"]["create_date"]
            # hit_dict["url"] = hit["_source"]["url"]
            # 根据索引类型处理不同的字段
            if s_type == "article":
                print("search进入article--hit")
                if "title" in hit["highlight"]:
                    hit_dict["title"] = "".join(hit["highlight"]["title"])
                else:
                    hit_dict["title"] = hit["_source"]["title"]

                if "content" in hit["highlight"]:
                    hit_dict["content"] = "".join(hit["highlight"]["content"])[:500]
                else:
                    hit_dict["content"] = hit["_source"]["content"][:500]

                hit_dict["create_date"] = hit["_source"]["create_date"]
                hit_dict["url"] = hit["_source"]["url"]
            elif s_type == "author":
                print("search进入author--hit")
                if "name" in hit["highlight"]:
                    hit_dict["name"] = "".join(hit["highlight"]["name"])
                else:
                    hit_dict["name"] = hit["_source"]["name"]

                if "bio" in hit["highlight"]:
                    hit_dict["bio"] = "".join(hit["highlight"]["bio"])[:500]
                else:
                    hit_dict["bio"] = hit["_source"]["bio"][:500]

                if "signature" in hit["highlight"]:
                    hit_dict["signature"] = "".join(hit["highlight"]["signature"])
                else:
                    hit_dict["signature"] = hit["_source"]["signature"]

                hit_dict["img_url"] = hit["_source"]["img_url"]
                hit_dict["article_count"] = hit["_source"]["article_count"]
                hit_dict["followers_count"] = hit["_source"]["followers_count"]

            hit_dict["score"] = hit["_score"]

            hit_list.append(hit_dict)

            #print("search内部：", hit_list)

        return render(request, "result.html", {"page": page,
                                               "all_hits": hit_list,
                                               "key_words": key_words,
                                               "total_nums": total_nums,
                                               "page_nums": page_nums,
                                               "last_seconds": last_seconds,
                                               # "jobbole_count": jobbole_count,
                                               "article_count": article_count,
                                               "s_type": s_type,
                                               })
