from django.db import models


# 1. 导入所需模块***********************************************
# Create your models here.
from datetime import datetime
# InnerObjectWrapper
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer,  Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

# 创建与本地 Elasticsearch 实例的连接*************************************
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])


# 2. 自定义分析器******************************************
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


# 3. 定义 IK 分词器*************************************
# ik_analyzer 是一个自定义的分析器，它使用了 IK 分词器（ik_max_word），这是一个常用的中文分词器，可以有效地分词中文文本。
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

# 4. 定义 Elasticsearch 文档类型：ArticleType****************************************
class ArticleType(DocType):
    # 伯乐在线文章类型
    suggest = Completion(analyzer=ik_analyzer)  # 用于定义自动补全建议
    title = Text(analyzer="ik_max_word")  # title 字段存储文章的标题，类型为 Text，表示它是一个全文检索字段，使用 ik_max_word 分词器分析文本。
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")  # tags 字段表示文章的标签，使用 ik_max_word 分词器进行分析。
    content = Text(analyzer="ik_max_word")  # content = Text(analyzer="ik_max_word")：content 字段表示文章的内容，同样使用 ik_max_word 分词器进行分析。

    class Meta:
        index = "jobbole"  # 定义 Elasticsearch 中索引的名称
        doc_type = "article"  # 定义文档的类型名称

if __name__ == "__main__":
    ArticleType.init()
