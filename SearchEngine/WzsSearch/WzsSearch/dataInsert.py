from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from datetime import datetime
from models import ArticleType  # 引用之前定义的 ArticleType 类

# -*- coding: utf-8 -*-
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

data_xinxi_dj=[
    {
        "title": "信息检索基础与实践",
        "create_date": "2024-07-01",
        "url": "https://example.com/infosearch",
        "url_object_id": "234abc",
        "front_image_url": "https://example.com/image12.jpg",
        "front_image_path": "/path/to/image12.jpg",
        "praise_nums": 520,
        "comment_nums": 160,
        "fav_nums": 390,
        "tags": ["信息检索", "搜索引擎", "数据处理"],
        "content": "本书介绍了信息检索的基础理论和实际应用，涵盖了检索模型、搜索引擎的工作原理以及如何处理和优化数据。书中通过案例分析了从简单的关键词匹配到复杂的自然语言处理（NLP"
                   "）技术在信息检索中的应用。特别是在大数据时代，如何高效处理海量数据并提升检索精度和速度，书中也有详细讲解。适合对信息检索和搜索引擎优化（SEO）感兴趣的读者。",
        "suggest": ["搜索引擎优化", "NLP 基础", "大数据处理"],
        "weight": 5
    },
    {
        "title": "Django Web 开发实战",
        "create_date": "2024-08-15",
        "url": "https://example.com/django-web",
        "url_object_id": "567xyz",
        "front_image_url": "https://example.com/image13.jpg",
        "front_image_path": "/path/to/image13.jpg",
        "praise_nums": 600,
        "comment_nums": 180,
        "fav_nums": 450,
        "tags": ["Django", "Web 开发", "Python"],
        "content": "本书是 Django Web 开发的实战指南，旨在帮助开发者快速上手 Django 框架并进行实际项目开发。内容包括 Django 的基础知识、模型与视图的设计、路由控制、模板渲染等核心概念，以及如何与数据库进行交互、用户认证与授权、文件上传等功能实现。书中还介绍了如何使用 Django Rest Framework (DRF) 构建 API 和前后端分离开发，适合希望深入学习 Django 的开发者。",
        "suggest": ["Django 入门", "Web 开发教程", "Python 后端开发"],
        "weight": 6
    },

    {
        "title": "Django 高级编程与优化",
        "create_date": "2024-08-30",
        "url": "https://example.com/django-advanced",
        "url_object_id": "123mno",
        "front_image_url": "https://example.com/image15.jpg",
        "front_image_path": "/path/to/image15.jpg",
        "praise_nums": 510,
        "comment_nums": 200,
        "fav_nums": 420,
        "tags": ["Django", "优化", "性能"],
        "content": "本书介绍了 Django 框架中的高级编程技术，涵盖了 Django 性能优化的常用技巧、数据库查询优化、缓存技术、异步处理、以及如何扩展 Django 系统以应对高并发的访问量。书中详细阐述了如何进行 Django 项目的调试与测试，以及如何在生产环境中部署高效稳定的 Django Web 应用。适合希望提升 Django 开发效率和性能的高级开发者。",
        "suggest": ["Django 性能优化", "Web 应用部署", "Python 高级编程"],
        "weight": 5
    }
]

data_javaScript=[
    {
        "title": "深入浅出 JavaScript",
        "create_date": "2024-07-22",
        "url": "https://example.com/deep-js",
        "url_object_id": "230abc",
        "front_image_url": "https://example.com/image12.jpg",
        "front_image_path": "/path/to/image12.jpg",
        "praise_nums": 320,
        "comment_nums": 95,
        "fav_nums": 220,
        "tags": ["JavaScript", "前端开发", "编程"],
        "content": "本书深入探讨了 JavaScript 语言的核心概念，包括作用域、闭包、异步编程、事件循环等。通过一系列实际案例，帮助读者理解 JavaScript 内部机制，并掌握如何在实际项目中高效使用这些概念。此外，还涉及了 ES6 新特性、模块化开发等内容，适合前端开发人员及任何有 JavaScript 基础的程序员。",
        "suggest": ["JavaScript 基础", "前端开发教程", "ES6 学习"],
        "weight": 5
    },
    {
        "title": "现代 JavaScript 开发",
        "create_date": "2024-08-10",
        "url": "https://example.com/modern-js",
        "url_object_id": "541xyz",
        "front_image_url": "https://example.com/image13.jpg",
        "front_image_path": "/path/to/image13.jpg",
        "praise_nums": 540,
        "comment_nums": 210,
        "fav_nums": 410,
        "tags": ["JavaScript", "ES6", "React"],
        "content": "本书介绍了现代 JavaScript 开发中的前沿技术，包括 ES6+ 新特性、React 框架的使用、模块化开发及工具链的配置等。通过多个示例项目，详细讲解了如何使用 JavaScript 构建单页面应用（SPA），并掌握常见的前端开发流程与工具。适合想要提升 JavaScript 技能的开发者以及前端工程师。",
        "suggest": ["React 教程", "ES6 新特性", "前端开发工具链"],
        "weight": 6
    },
    {
        "title": "JavaScript 高级编程技巧",
        "create_date": "2024-09-05",
        "url": "https://example.com/advanced-js",
        "url_object_id": "674pqr",
        "front_image_url": "https://example.com/image14.jpg",
        "front_image_path": "/path/to/image14.jpg",
        "praise_nums": 380,
        "comment_nums": 180,
        "fav_nums": 300,
        "tags": ["JavaScript", "编程技巧", "性能优化"],
        "content": "这本书深入探讨了 JavaScript 编程中的高级技巧与常见难题，内容涵盖了性能优化、内存管理、复杂数据结构的处理、异步编程的最佳实践等。作者通过实际的项目案例，展示了如何提高 JavaScript 代码的效率和可维护性。适合有一定 JavaScript 基础的开发者，尤其是对性能优化和高效编程有兴趣的开发人员。",
        "suggest": ["JavaScript 性能优化", "高级编程技巧", "异步编程"],
        "weight": 5
    },
    {
        "title": "JavaScript 与 Node.js 实践",
        "create_date": "2024-07-30",
        "url": "https://example.com/js-node",
        "url_object_id": "890hij",
        "front_image_url": "https://example.com/image15.jpg",
        "front_image_path": "/path/to/image15.jpg",
        "praise_nums": 420,
        "comment_nums": 160,
        "fav_nums": 350,
        "tags": ["JavaScript", "Node.js", "后端开发"],
        "content": "本书从前端开发的角度介绍了如何使用 Node.js 构建高效的后端应用。通过学习如何在 Node.js 中处理 HTTP 请求、文件系统操作、数据库连接等基础知识，读者将能够快速上手并使用 JavaScript 进行全栈开发。此外，还介绍了如何与前端框架（如 React）进行无缝集成，实现前后端一体化开发。",
        "suggest": ["Node.js 入门", "JavaScript 全栈开发", "后端开发教程"],
        "weight": 5
    },
    {
        "title": "JavaScript 数据结构与算法",
        "create_date": "2024-09-18",
        "url": "https://example.com/js-algorithms",
        "url_object_id": "342lmn",
        "front_image_url": "https://example.com/image16.jpg",
        "front_image_path": "/path/to/image16.jpg",
        "praise_nums": 500,
        "comment_nums": 250,
        "fav_nums": 420,
        "tags": ["JavaScript", "数据结构", "算法"],
        "content": "这本书专注于 JavaScript 中的数据结构与算法。通过循序渐进的讲解，从数组、链表、栈、队列到更复杂的图、树、堆等数据结构，帮助读者掌握常见的编程思路。书中还提供了丰富的算法题，帮助读者掌握排序、查找、动态规划等常见算法，并通过 JavaScript 实现，增强读者的编程能力。",
        "suggest": ["数据结构与算法", "JavaScript 算法", "编程面试"],
        "weight": 6
    }
]

data_react=[
{
    "title": "深入学习 React 应用开发",
    "create_date": "2024-07-20",
    "url": "https://example.com/react-app",
    "url_object_id": "130abc",
    "front_image_url": "https://example.com/image12.jpg",
    "front_image_path": "/path/to/image12.jpg",
    "praise_nums": 500,
    "comment_nums": 150,
    "fav_nums": 400,
    "tags": ["React", "前端开发", "JavaScript"],
    "content": "本书详细介绍了如何使用 React 构建现代化的单页应用（SPA）。从基础的组件构建到复杂的状态管理，书中不仅包含理论部分，还通过丰富的案例展示了如何在实际项目中应用 React。特别地，书中还探讨了 React 生态中的工具，如 React Router、Redux、Hooks 等，帮助开发者更高效地开发 Web 应用。",
    "suggest": ["React 框架", "前端工程化", "React Hooks 教程"],
    "weight": 6
},
{
    "title": "React 性能优化实战",
    "create_date": "2024-08-10",
    "url": "https://example.com/react-performance",
    "url_object_id": "131def",
    "front_image_url": "https://example.com/image13.jpg",
    "front_image_path": "/path/to/image13.jpg",
    "praise_nums": 320,
    "comment_nums": 80,
    "fav_nums": 290,
    "tags": ["React", "性能优化", "前端技术"],
    "content": "本书专注于 React 应用中的性能优化，涵盖了从渲染优化、代码分割、懒加载到服务器端渲染（SSR）等多种性能提升技术。通过详细的案例分析和实战技巧，读者可以学习如何识别性能瓶颈、使用开发工具进行性能调试，以及如何使用 React 官方工具和第三方库提高应用响应速度和用户体验。",
    "suggest": ["前端性能优化", "React 组件优化", "性能调试工具"],
    "weight": 4
},
{
    "title": "React Native 跨平台移动应用开发",
    "create_date": "2024-09-05",
    "url": "https://example.com/react-native",
    "url_object_id": "132ghi",
    "front_image_url": "https://example.com/image14.jpg",
    "front_image_path": "/path/to/image14.jpg",
    "praise_nums": 600,
    "comment_nums": 180,
    "fav_nums": 500,
    "tags": ["React Native", "移动开发", "跨平台应用"],
    "content": "本书专门针对 React Native 开发跨平台移动应用的技巧与最佳实践。书中从基础的 React Native 设置，到高级的原生模块集成，提供了完整的开发流程和实用的技巧。重点介绍了如何在 iOS 和 Android 平台上编写高效、流畅的移动应用，特别是在性能、调试、用户体验和跨平台兼容性方面的处理。",
    "suggest": ["React Native 教程", "移动应用开发", "跨平台开发框架"],
    "weight": 7
},
{
    "title": "React 与 Redux 完全指南",
    "create_date": "2024-10-12",
    "url": "https://example.com/react-redux",
    "url_object_id": "133jkl",
    "front_image_url": "https://example.com/image15.jpg",
    "front_image_path": "/path/to/image15.jpg",
    "praise_nums": 400,
    "comment_nums": 120,
    "fav_nums": 350,
    "tags": ["React", "Redux", "状态管理"],
    "content": "本书从零开始详细讲解了如何在 React 项目中使用 Redux 进行状态管理。通过通俗易懂的例子和逐步引导，读者将学会如何利用 Redux 中的核心概念，如 Store、Action、Reducer 和 Middleware 来组织应用的状态。书中还特别强调了如何在实际项目中解决异步数据流的挑战，并结合 React-Redux 的最佳实践，帮助开发者在实际开发中提高效率。",
    "suggest": ["React 状态管理", "Redux 入门", "前端开发架构"],
    "weight": 5
}

]

# 向 Elasticsearch 插入数据
def insert_data():
    for article in data_react:
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
