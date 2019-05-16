# -*- coding:utf-8 -*-
"""
created by goblinM 2019.5.15
2.情感定位
"""


def classifyWords(wordDict):
    # 1 情感词
    sen_dict = {}
    with open(r'wordfiles/BosonNLP_sentiment_score.txt','r',encoding='utf-8') as f:
        for data in f.readlines():
            data = data.split('\n')[0]
            sen_dict.setdefault(data.split(' ')[0],data.split(' ')[1])
    print(sen_dict)

    # 2 否定词
    # 3 程度副词
    degree_dict = {}
    with open(r'wordfiles/degree.txt','r',encoding='utf-8') as f:
        for data in f.readlines():
            degree_dict.set