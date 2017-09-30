#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /home/jx/Desktop/codes/AI/UrlToUrl/code/bfsFind.py
# Project: /home/jx/Desktop/codes/AI/UrlToUrl
# Created Date: Thursday, September 28th 2017, 11:00:17 pm
# Author: JX
# -----
# Last Modified: Sat Sep 30 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# All shall be well and all shall be well and all manner of things shall be well.
# We're doomed!
###
from tools import *
from datetime import datetime

def optBfs(startLink,targetList):
    stepNum = 0
    openList = [{'link':startLink, 'dis':0, 'path':[]}]
    visitedLise = []
    while (len(openList)!=0):
        sourceLink = dict(openList[0])
        visitedLise.append(sourceLink['link'])
        stepNum += 1    
        if (sourceLink['link'].find(targetList)!=-1):
            return (sourceLink['path']+[sourceLink['link']],stepNum)
        del openList[0]
        openList.extend(getAllLink(targetList, sourceLink, visitedLise))
        openList.sort(key=lambda obj:obj.get('dis'), reverse=False)
    return (['NULL'], stepNum)
    
if __name__ == '__main__':
    startTime = datetime.now()
    ans=optBfs('https://www.hao123.com/', 'http://sports.sina.com.cn/g/ucl/fixtures.html')
    endTime = datetime.now()
    print('搜索路径为:'+str(ans[0]))
    print('共搜索了%d个网页.' % ans[1])
    print('共用时%d秒:'%(endTime-startTime).seconds)