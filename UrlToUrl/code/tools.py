#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /home/jx/Desktop/codes/AI/UrlToUrl/code/tools.py
# Project: /home/jx/Desktop/codes/AI/UrlToUrl
# Created Date: Thursday, September 28th 2017, 11:06:43 pm
# Author: JX
# -----
# Last Modified: Fri Sep 29 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# All shall be well and all shall be well and all manner of things shall be well.
# We're doomed!
###
import requests
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def getAllLink(targetLink,sourceLink, *visitedLinks):
    """
    获取当前页面的所有链接
        :param sourceLink: 本页面就是要获取这个页面的所有链接
        :param targetLink: 目标的界面
    """
    headers={
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    try:
        html = requests.get(url=sourceLink['link'], headers=headers, verify=False).text
    except:
        return []
    ans = []
    xnodes = etree.HTML(html);
    links = xnodes.xpath('//a/@href')
    for link in links:
        if (link == "#"):
            continue
        if (link.find('javascript')!=-1):
            continue
        if (link in visitedLinks):
            continue
        if (link.find('http') == -1):
            link = sourceLink['link'] +'/'+link
        tp = []
        tp.extend(sourceLink['path'])
        tp.append(sourceLink['link'])
        ans.append({'link':link, 'dis':getDis(str(targetLink), str(link)), 'path': tp})
    # ans.sort(key=lambda obj:obj.get('dis'), reverse=False)
    return ans

def getDis(targetLink, curLink):
    """
    获取2个url之间的文本距离,文本可以有插入删除替换3种操作 使用dp算法
    算法详情见:https://discuss.leetcode.com/topic/101598/python-dp-solution-that-beats-57-58
        :param targetLink: 源url
        :param curLink: 目标url
    """
    m, n = len(targetLink), len(curLink)
    r = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m or j == n:
                r[i][j] = max(m-i, n-j)
            elif targetLink[i] == curLink[j]:
                r[i][j] = r[i+1][j+1]
            else:
                r[i][j] = 1 + min(r[i+1][j], r[i][j+1], r[i+1][j+1])
    return r[0][0]