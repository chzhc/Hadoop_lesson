#!/usr/bin/env python
# coding=utf-8
import sys,os
import jieba

all_line=[]
for line in sys.stdin:  # 遍历读入数据的每一行
    line = line.replace(' ','') # 将多余的空格去除
    line = line.replace('.','') # 将多余的符号去除
    words = line.split("\t")    # 按tab将句子分割成单个单词
    all_line.append(words[2])
all_line.sort() # 进行内部排序
for line in all_line:
    print ('%s\t%s' %(line, 1)) # 流式输出
    
