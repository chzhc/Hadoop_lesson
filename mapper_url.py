#!/usr/bin/env python
# coding=utf-8
import sys,os
import jieba

for line in sys.stdin:  # 遍历读入数据的每一行
    line = line.replace(' ','')     # 将多余的空格去除
    words = line.split("\t")        #按tab将句子分割成单个
    #cut=jieba.cut(words[5])
    #for word in words:
    print ('%s\t%s' %(words[5], 1))
    # print("")

