#!/usr/bin/env python
# coding=utf-8
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# 输入必须经过预先排序
for line in sys.stdin:
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError: 
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print "%s\t%s" % (current_word, current_count)
        current_count = count
        current_word = word

if word == current_word:    # 流式输出（无序）
    print "%s\t%s" % (current_word, current_count)
    
