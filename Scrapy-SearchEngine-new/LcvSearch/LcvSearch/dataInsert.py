from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from datetime import datetime
from models import ArticleType  # 引用之前定义的 ArticleType 类


# 建立连接
connections.create_connection(hosts=["localhost"])

# 创建 Elasticsearch 客户端
client = Elasticsearch(hosts=["127.0.0.1"])

# 模拟一些数据
data = [
    {
        "title": "如何使用 Elasticsearch 进行搜索",
        "create_date": datetime.now(),
        "url": "http://example.com/1",
        "url_object_id": "1",
        "front_image_url": "http://example.com/1.jpg",
        "front_image_path": "/images/1.jpg",
        "praise_nums": 100,
        "comment_nums": 20,
        "fav_nums": 50,
        "tags": ["elasticsearch", "search", "tutorial"],
        "content": "这是一些关于 Elasticsearch 的内容，用于演示如何在系统中进行搜索。",
    },
    {
        "title": "Django 与 Elasticsearch 集成",
        "create_date": datetime.now(),
        "url": "http://example.com/2",
        "url_object_id": "2",
        "front_image_url": "http://example.com/2.jpg",
        "front_image_path": "/images/2.jpg",
        "praise_nums": 150,
        "comment_nums": 35,
        "fav_nums": 60,
        "tags": ["django", "elasticsearch", "tutorial"],
        "content": "介绍如何将 Django 与 Elasticsearch 集成，实现强大的搜索功能。",
    },
    {
        "title": "深入理解 Elasticsearch 分词器",
        "create_date": datetime.now(),
        "url": "http://example.com/3",
        "url_object_id": "3",
        "front_image_url": "http://example.com/3.jpg",
        "front_image_path": "/images/3.jpg",
        "praise_nums": 200,
        "comment_nums": 50,
        "fav_nums": 80,
        "tags": ["elasticsearch", "analyzer", "search"],
        "content": "本篇文章将介绍 Elasticsearch 中的分词器，并演示如何自定义分词器。",
    },
]

data1 = [
    {
        "title": "人工智能的未来：从机器学习到深度学习的演变",
        "create_date": datetime.now(),
        "url": "http://example.com/ai-future",
        "url_object_id": "2",
        "front_image_url": "http://example.com/ai-future.jpg",
        "front_image_path": "/images/ai-future.jpg",
        "praise_nums": 200,
        "comment_nums": 40,
        "fav_nums": 80,
        "tags": ["artificial intelligence", "machine learning", "deep learning"],
        "content": "本文探讨了人工智能的未来发展，分析了从传统机器学习到深度学习的演变，并展望了AI在各个领域的应用。"
    },
    {
        "title": "大数据时代：如何利用数据驱动决策",
        "create_date": datetime.now(),
        "url": "http://example.com/big-data-decision",
        "url_object_id": "3",
        "front_image_url": "http://example.com/big-data.jpg",
        "front_image_path": "/images/big-data.jpg",
        "praise_nums": 150,
        "comment_nums": 30,
        "fav_nums": 60,
        "tags": ["big data", "data science", "business intelligence"],
        "content": "大数据正改变着我们的决策方式。本文将讨论如何通过数据挖掘与分析提高商业决策效率。"
    },
    {
        "title": "UI设计中的用户体验：从界面到交互的演变",
        "create_date": datetime.now(),
        "url": "http://example.com/ui-design",
        "url_object_id": "4",
        "front_image_url": "http://example.com/ui-design.jpg",
        "front_image_path": "/images/ui-design.jpg",
        "praise_nums": 180,
        "comment_nums": 50,
        "fav_nums": 90,
        "tags": ["UI design", "user experience", "interaction design"],
        "content": "UI设计不仅是界面美学，更是用户体验的核心。本文深入探讨了UI设计中用户体验的重要性，并提供了最佳实践。"
    },
    {
        "title": "深度学习：改变图像识别的游戏规则",
        "create_date": datetime.now(),
        "url": "http://example.com/deep-learning-image-recognition",
        "url_object_id": "5",
        "front_image_url": "http://example.com/deep-learning.jpg",
        "front_image_path": "/images/deep-learning.jpg",
        "praise_nums": 220,
        "comment_nums": 60,
        "fav_nums": 120,
        "tags": ["deep learning", "image recognition", "computer vision"],
        "content": "本文介绍了深度学习如何改变图像识别技术的现状，包括卷积神经网络(CNN)的应用及其在计算机视觉中的突破性进展。"
    },
    {
        "title": "大数据与机器学习的结合：如何实现智能预测",
        "create_date": datetime.now(),
        "url": "http://example.com/big-data-ml",
        "url_object_id": "6",
        "front_image_url": "http://example.com/big-data-ml.jpg",
        "front_image_path": "/images/big-data-ml.jpg",
        "praise_nums": 250,
        "comment_nums": 70,
        "fav_nums": 130,
        "tags": ["big data", "machine learning", "predictive analytics"],
        "content": "随着大数据和机器学习技术的发展，企业能够更准确地预测未来趋势。本文探讨了这两者如何结合，推动智能预测的实现。"
    },
    {
        "title": "交互设计：如何打造用户友好的产品体验",
        "create_date": datetime.now(),
        "url": "http://example.com/interaction-design",
        "url_object_id": "7",
        "front_image_url": "http://example.com/interaction-design.jpg",
        "front_image_path": "/images/interaction-design.jpg",
        "praise_nums": 160,
        "comment_nums": 40,
        "fav_nums": 70,
        "tags": ["interaction design", "user experience", "product design"],
        "content": "交互设计是提升产品用户体验的重要组成部分。本文介绍了交互设计的基本原则，以及如何在实际产品中应用这些原则。"
    },
    {
        "title": "区块链技术：超越加密货币的应用前景",
        "create_date": datetime.now(),
        "url": "http://example.com/blockchain",
        "url_object_id": "8",
        "front_image_url": "http://example.com/blockchain.jpg",
        "front_image_path": "/images/blockchain.jpg",
        "praise_nums": 190,
        "comment_nums": 50,
        "fav_nums": 110,
        "tags": ["blockchain", "cryptocurrency", "distributed ledger"],
        "content": "区块链技术的应用远远超出了加密货币的范畴。本文将探讨区块链如何变革供应链管理、金融、医疗等多个领域。"
    }
]

data2 = [
    {
        "title": "机器学习中的监督学习与无监督学习",
        "create_date": datetime.now(),
        "url": "http://example.com/supervised-vs-unsupervised",
        "url_object_id": "9",
        "front_image_url": "http://example.com/supervised-vs-unsupervised.jpg",
        "front_image_path": "/images/supervised-vs-unsupervised.jpg",
        "praise_nums": 300,
        "comment_nums": 80,
        "fav_nums": 150,
        "tags": ["machine learning", "supervised learning", "unsupervised learning"],
        "content": "在机器学习中，监督学习和无监督学习是两种常见的学习方法。监督学习使用已标注的数据来训练模型，目的是根据已知标签预测未知数据的标签。而无监督学习则通过未标注的数据发现数据中的隐藏模式。本文将详细介绍这两种学习方式的原理、应用场景以及它们之间的主要区别。"
    },
    {
        "title": "大数据处理技术：Hadoop与Spark的对比",
        "create_date": datetime.now(),
        "url": "http://example.com/hadoop-vs-spark",
        "url_object_id": "10",
        "front_image_url": "http://example.com/hadoop-vs-spark.jpg",
        "front_image_path": "/images/hadoop-vs-spark.jpg",
        "praise_nums": 220,
        "comment_nums": 60,
        "fav_nums": 130,
        "tags": ["big data", "Hadoop", "Spark", "data processing"],
        "content": "随着大数据技术的迅速发展，Hadoop 和 Spark 已经成为最流行的大数据处理框架。Hadoop 是一个分布式存储和计算平台，适用于批处理任务，而 Spark 则是一种更加高效的实时数据处理框架，能够处理实时流数据。本文将详细分析 Hadoop 和 Spark 的优缺点，帮助您了解它们的最佳应用场景。"
    },
    {
        "title": "深度学习中的卷积神经网络（CNN）",
        "create_date": datetime.now(),
        "url": "http://example.com/cnn-in-deep-learning",
        "url_object_id": "11",
        "front_image_url": "http://example.com/cnn-in-deep-learning.jpg",
        "front_image_path": "/images/cnn-in-deep-learning.jpg",
        "praise_nums": 350,
        "comment_nums": 90,
        "fav_nums": 180,
        "tags": ["deep learning", "CNN", "neural networks", "image recognition"],
        "content": "卷积神经网络（CNN）是深度学习中的一种重要模型，特别在图像处理和计算机视觉任务中取得了显著的成绩。CNN 的关键特性是其能够自动提取图像中的特征，而不需要人工设计特征提取算法。本文将深入介绍 CNN 的工作原理、结构、训练过程以及在实际应用中的典型案例，例如图像分类、目标检测等。"
    },
    {
        "title": "云计算与虚拟化技术：从基础架构到平台即服务（PaaS）",
        "create_date": datetime.now(),
        "url": "http://example.com/cloud-computing-and-virtualization",
        "url_object_id": "12",
        "front_image_url": "http://example.com/cloud-computing.jpg",
        "front_image_path": "/images/cloud-computing.jpg",
        "praise_nums": 280,
        "comment_nums": 70,
        "fav_nums": 140,
        "tags": ["cloud computing", "virtualization", "IaaS", "PaaS", "SaaS"],
        "content": "云计算是现代IT基础设施的重要组成部分，它通过虚拟化技术将计算资源（如存储、计算能力）以服务的形式提供给用户。虚拟化技术使得云计算能够灵活地提供资源，而无需企业自己维护物理硬件。本文将介绍云计算的基本概念，探讨基础架构即服务（IaaS）、平台即服务（PaaS）和软件即服务（SaaS）的不同，以及它们的典型应用案例。"
    },
    {
        "title": "UI设计中的响应式设计：适应多设备的界面设计",
        "create_date": datetime.now(),
        "url": "http://example.com/responsive-design",
        "url_object_id": "13",
        "front_image_url": "http://example.com/responsive-design.jpg",
        "front_image_path": "/images/responsive-design.jpg",
        "praise_nums": 210,
        "comment_nums": 50,
        "fav_nums": 100,
        "tags": ["UI design", "responsive design", "web design"],
        "content": "响应式设计是当今 UI 设计中的一种重要趋势。它使得网页能够根据不同设备的屏幕大小自动调整布局，从而提高用户体验。随着移动设备的普及，响应式设计已经成为设计师必须掌握的技能。本文将介绍响应式设计的基本原理，探讨如何使用 CSS 媒体查询和灵活布局来实现响应式网页设计，并提供一些实践中的设计技巧。"
    },
    {
        "title": "区块链技术的去中心化原理",
        "create_date": datetime.now(),
        "url": "http://example.com/blockchain-decentralization",
        "url_object_id": "14",
        "front_image_url": "http://example.com/blockchain-decentralization.jpg",
        "front_image_path": "/images/blockchain-decentralization.jpg",
        "praise_nums": 250,
        "comment_nums": 65,
        "fav_nums": 130,
        "tags": ["blockchain", "decentralization", "cryptocurrency", "distributed ledger"],
        "content": "区块链是一种去中心化的分布式账本技术，它通过加密算法保证数据的安全性和不可篡改性。在传统的中心化系统中，所有的数据都存储在一个中心服务器上，而区块链则通过多个节点分布式存储数据，从而消除了单点故障的风险。本文将介绍区块链的去中心化原理，分析其在金融、供应链管理等行业中的应用，以及它如何改变传统的商业模式。"
    },
    {
        "title": "5G技术的到来对物联网（IoT）的影响",
        "create_date": datetime.now(),
        "url": "http://example.com/5g-and-iot",
        "url_object_id": "15",
        "front_image_url": "http://example.com/5g-and-iot.jpg",
        "front_image_path": "/images/5g-and-iot.jpg",
        "praise_nums": 230,
        "comment_nums": 60,
        "fav_nums": 120,
        "tags": ["5G", "IoT", "internet of things", "telecommunication"],
        "content": "5G 技术将显著提高物联网（IoT）设备之间的通信效率，使得物联网的应用场景更加广泛。随着 5G 网络的铺开，智能家居、自动驾驶、工业物联网等将获得更高的带宽和更低的延迟，带来前所未有的变革。本文将探讨 5G 技术如何促进 IoT 发展，以及它如何影响各行各业，包括智慧城市、智能制造、远程医疗等。"
    },
    {
        "title": "自动化测试工具的选择与实践",
        "create_date": datetime.now(),
        "url": "http://example.com/automation-testing-tools",
        "url_object_id": "16",
        "front_image_url": "http://example.com/automation-testing-tools.jpg",
        "front_image_path": "/images/automation-testing-tools.jpg",
        "praise_nums": 190,
        "comment_nums": 45,
        "fav_nums": 95,
        "tags": ["automation testing", "QA", "software testing"],
        "content": "随着软件开发周期的加速，自动化测试已经成为保证软件质量的一个重要环节。自动化测试工具可以帮助开发团队高效地完成回归测试、性能测试等任务，减少人为错误，提高测试效率。本文将介绍几种流行的自动化测试工具，并探讨它们在实际项目中的应用，包括 Selenium、JUnit、Appium 等工具的优缺点。"
    }
]

dataWithSuggest1 = [
    {
        "title": "Python 编程指南",
        "create_date": "2024-12-01",
        "url": "https://example.com/python",
        "url_object_id": "123abc",
        "front_image_url": "https://example.com/image.jpg",
        "front_image_path": "/path/to/image.jpg",
        "praise_nums": 250,
        "comment_nums": 40,
        "fav_nums": 150,
        "tags": ["Python", "编程", "技术"],
        "content": "这是一本全面介绍 Python 编程的书籍。",
        "suggest": ["Python 基础", "编程入门", "Python 教程"],  # 自定义补全值
        "weight": 5
    },
    {
        "title": "Python 数据分析入门",
        "create_date": "2024-12-01",
        "url": "https://example.com/python-data",
        "url_object_id": "456def",
        "front_image_url": "https://example.com/image1.jpg",
        "front_image_path": "/path/to/image1.jpg",
        "praise_nums": 340,
        "comment_nums": 50,
        "fav_nums": 200,
        "tags": ["Python", "数据分析", "技术"],
        "content": "本书详细介绍了如何使用 Python 进行数据分析，包括 Pandas、NumPy、Matplotlib 等主流工具的使用，以及常见的数据清洗、可视化和建模方法。",
        "suggest": ["Python 数据分析", "数据清洗教程", "Python 可视化"],
        "weight": 4
    },
    {
        "title": "人工智能与机器学习实战",
        "create_date": "2024-11-15",
        "url": "https://example.com/ai-ml",
        "url_object_id": "789ghi",
        "front_image_url": "https://example.com/image2.jpg",
        "front_image_path": "/path/to/image2.jpg",
        "praise_nums": 560,
        "comment_nums": 120,
        "fav_nums": 400,
        "tags": ["人工智能", "机器学习", "深度学习"],
        "content": "本书深入探讨了机器学习和深度学习的核心算法，包括线性回归、决策树、神经网络、卷积神经网络等。同时通过 TensorFlow 和 PyTorch 提供了实战案例。",
        "suggest": ["机器学习入门", "深度学习指南", "AI 项目实战"],
        "weight": 5
    },
    {
        "title": "大数据处理与 Hadoop 技术",
        "create_date": "2024-10-10",
        "url": "https://example.com/bigdata",
        "url_object_id": "101jkl",
        "front_image_url": "https://example.com/image3.jpg",
        "front_image_path": "/path/to/image3.jpg",
        "praise_nums": 420,
        "comment_nums": 60,
        "fav_nums": 300,
        "tags": ["大数据", "Hadoop", "分布式系统"],
        "content": "本书介绍了大数据领域的基础知识和实践技术，涵盖 Hadoop 架构、HDFS 分布式文件系统、MapReduce 编程模型，以及 Hive 和 Spark 的应用。",
        "suggest": ["大数据入门", "Hadoop 架构", "分布式数据存储"],
        "weight": 4
    },
    {
        "title": "网络安全基础与攻防实战",
        "create_date": "2024-09-05",
        "url": "https://example.com/cybersecurity",
        "url_object_id": "112mno",
        "front_image_url": "https://example.com/image4.jpg",
        "front_image_path": "/path/to/image4.jpg",
        "praise_nums": 380,
        "comment_nums": 80,
        "fav_nums": 260,
        "tags": ["网络安全", "黑客技术", "漏洞扫描"],
        "content": "本书介绍了网络安全领域的基础理论和攻防技术，包括常见的攻击方式如 SQL 注入、XSS、CSRF 等，以及如何使用工具如 Metasploit 和 Nmap 进行漏洞扫描和渗透测试。",
        "suggest": ["网络安全教程", "漏洞挖掘", "渗透测试指南"],
        "weight": 5
    },
    {
        "title": "前端开发从入门到精通",
        "create_date": "2024-08-20",
        "url": "https://example.com/frontend",
        "url_object_id": "123pqr",
        "front_image_url": "https://example.com/image5.jpg",
        "front_image_path": "/path/to/image5.jpg",
        "praise_nums": 500,
        "comment_nums": 100,
        "fav_nums": 350,
        "tags": ["前端开发", "JavaScript", "HTML5"],
        "content": "本书从基础到高级介绍了前端开发技术，包括 HTML5、CSS3 和 JavaScript 的核心知识，以及如何使用 Vue.js 和 React 构建现代化的前端应用。",
        "suggest": ["前端开发指南", "JavaScript 教程", "Vue.js 入门"],
        "weight": 4
    }
    ]


dataWithSuggest2 = [
    {
        "title": "全栈开发指南",
        "create_date": "2024-09-15",
        "url": "https://example.com/fullstack",
        "url_object_id": "124xyz",
        "front_image_url": "https://example.com/image6.jpg",
        "front_image_path": "/path/to/image6.jpg",
        "praise_nums": 320,
        "comment_nums": 75,
        "fav_nums": 200,
        "tags": ["全栈开发", "Node.js", "React"],
        "content": "本书系统性地介绍了全栈开发的流程，从 Node.js 和 Express 后端框架开始，结合 React 和 Redux 构建现代前端应用。最后还包含数据库操作、用户认证等综合性案例。",
        "suggest": ["全栈开发", "Node.js 教程", "React 高级开发"],
        "weight": 5
    },
    {
        "title": "人工智能基础与实战",
        "create_date": "2024-07-10",
        "url": "https://example.com/ai",
        "url_object_id": "125abc",
        "front_image_url": "https://example.com/image7.jpg",
        "front_image_path": "/path/to/image7.jpg",
        "praise_nums": 420,
        "comment_nums": 120,
        "fav_nums": 300,
        "tags": ["人工智能", "机器学习", "深度学习"],
        "content": "本书从人工智能的基本概念入手，详细讲解了机器学习与深度学习的算法原理，并通过 TensorFlow 和 PyTorch 实现多个项目案例，包括图像分类和自然语言处理。",
        "suggest": ["AI 入门", "深度学习指南", "TensorFlow 教程"],
        "weight": 4
    },
    {
        "title": "云计算与大数据技术解析",
        "create_date": "2024-05-25",
        "url": "https://example.com/cloud",
        "url_object_id": "126def",
        "front_image_url": "https://example.com/image8.jpg",
        "front_image_path": "/path/to/image8.jpg",
        "praise_nums": 250,
        "comment_nums": 90,
        "fav_nums": 180,
        "tags": ["云计算", "大数据", "Hadoop"],
        "content": "书中介绍了云计算的基本架构和核心概念，详细说明了如何使用 AWS 和 Azure 构建云端服务，并结合 Hadoop 和 Spark 进行大数据分析，适合希望深入了解云计算的开发者。",
        "suggest": ["云计算教程", "大数据入门", "Hadoop 使用指南"],
        "weight": 3
    },
    {
        "title": "网络安全技术与实践",
        "create_date": "2024-03-18",
        "url": "https://example.com/security",
        "url_object_id": "127ghi",
        "front_image_url": "https://example.com/image9.jpg",
        "front_image_path": "/path/to/image9.jpg",
        "praise_nums": 400,
        "comment_nums": 110,
        "fav_nums": 250,
        "tags": ["网络安全", "渗透测试", "加密技术"],
        "content": "本书介绍了网络安全的理论知识，包括密码学基础、防火墙技术和安全协议，并结合实际案例详细讲解了渗透测试的方法和工具使用，如 Metasploit 和 Wireshark。",
        "suggest": ["网络安全教程", "渗透测试指南", "加密技术基础"],
        "weight": 5
    },
    {
        "title": "DevOps 实战指南",
        "create_date": "2024-01-30",
        "url": "https://example.com/devops",
        "url_object_id": "128jkl",
        "front_image_url": "https://example.com/image10.jpg",
        "front_image_path": "/path/to/image10.jpg",
        "praise_nums": 380,
        "comment_nums": 85,
        "fav_nums": 210,
        "tags": ["DevOps", "容器化", "CI/CD"],
        "content": "本书详细介绍了 DevOps 的理念和工具链，包括 Jenkins 的 CI/CD 管道设计，以及使用 Docker 和 Kubernetes 构建容器化应用程序，为开发和运维提供系统性的指导。",
        "suggest": ["DevOps 工具", "容器化指南", "CI/CD 教程"],
        "weight": 4
    },
    {
        "title": "数据科学与 Python 应用",
        "create_date": "2024-06-15",
        "url": "https://example.com/datascience",
        "url_object_id": "129mno",
        "front_image_url": "https://example.com/image11.jpg",
        "front_image_path": "/path/to/image11.jpg",
        "praise_nums": 450,
        "comment_nums": 130,
        "fav_nums": 340,
        "tags": ["数据科学", "Python", "数据分析"],
        "content": "书中以 Python 为基础，介绍了数据科学的基本方法和工具，包括 Pandas、NumPy 和 Matplotlib，并通过多个案例演示了如何分析和可视化数据，最后涉及机器学习模型的简单实现。",
        "suggest": ["数据分析教程", "Python 入门", "数据可视化指南"],
        "weight": 5
    }
    ]

# 向 Elasticsearch 插入数据
def insert_data():
    for article in dataWithSuggest2:
        # 使用 ArticleType 创建数据文档
        article_doc = ArticleType(
            title=article["title"],
            create_date=article["create_date"],
            url=article["url"],
            url_object_id=article["url_object_id"],
            front_image_url=article["front_image_url"],
            front_image_path=article["front_image_path"],
            praise_nums=article["praise_nums"],
            comment_nums=article["comment_nums"],
            fav_nums=article["fav_nums"],
            tags=article["tags"],
            content=article["content"],
            suggest={
                "input": article.get("suggest", []),  # 自定义值
                "weight": article.get("weight", 1)
            }
        )
        article_doc.save(index="jobbole")   # 保存到 Elasticsearch

# 执行数据插入
if __name__ == "__main__":
    insert_data()
    print("数据已成功插入到 Elasticsearch 中")
