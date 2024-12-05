信息检索实验

相关依赖：

```
pip install -r requires.txt
Django 2.1.5
elasticsearch==7.0.2
elasticsearch-dsl==7.0.0
SearchEngine20241129 python-3.8.20
```

相关下载：

```
elasticsearch-analysis-ik-7.7.1.zip
elasticsearch-7.7.1-windows-x86_64.zip  jdk-1.8
Redis-x64-5.0.14.1.zip
```

es相关操作：

```
http://localhost:9200/jobbole/_search?
http://localhost:9200/authors/_search?size=1000
http://localhost:9200/jobbole/_search?q=JavaScript
```

运行：
```
cmd redis-server
es bin目录下，双击.bat文件
```

