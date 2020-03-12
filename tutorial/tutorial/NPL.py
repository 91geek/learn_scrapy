# -*- coding: utf-8 -*-

import re
import numpy as np
import pandas as pd
# 字符编码模块
import codecs
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 匹配中文字符正则表达式
zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
# 加载文本数据,构建语料库
text = codecs.open('/Users/wanglei/Documents/python/learn_scrapy/tutorial/items.jl', 'r', 'utf8')
content = text.read()
text.close()

stat = []
# 停用词语
stop_words = set(['的', '和', '是', '在', '要', '为', '我们', '以', '把', '了', '到', '上', '有','昆明','云南省'])

# 分词
segs = jieba.cut(content)
for seg in segs:
    # 匹配中文字符
    if zh_pattern.search(seg):
        # 去除停用词
        if seg not in stop_words:
            stat.append({'from': '十九大', 'word': seg})

# print(stat)
# 分词结果存到数据框
stat_df = pd.DataFrame(stat)
print(stat_df)
# pivot_table 透视表
pt_stat = stat_df.pivot_table(index='word', columns='from', fill_value=0, aggfunc=np.size)
# 分词结果频率排序
# print(pt_stat.sort_index(by='十九大'))

# 设置词云字体
cloud = WordCloud(font_path='/System/Library/fonts/PingFang.ttc', background_color='white')
words = pt_stat['十九大'].to_dict()
print(words)
# 生成词云
cloud.fit_words(words)
plt.imshow(cloud)
plt.axis('off')
plt.show()