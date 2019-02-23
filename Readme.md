# Hadoop作业

2018年秋季学期大数据分析与存储作业，分析搜狗提供的500w用户数据

基于`python2.7` `hadoop 2.8.5`  

```bash
hadoop  jar $HADOOP_HOME/hadoop-streaming.jar
```

使用hadoop提供的Streaming方式，将数据使用python进行计算，各个词汇的统计

本次采用python脚本

依赖的是hadoop的流处理

其中分词部分已经注释，如果需要开启分词功能，需要使用pip install jieba作为分词工具