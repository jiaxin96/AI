#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /home/jx/Desktop/codes/AI/TSP/问题生成器/genMap.py
# Project: /home/jx/Desktop/codes/AI/TSP
# Created Date: Saturday, September 30th 2017, 7:50:25 pm
# Author: JX
# -----
# Last Modified: Mon Oct 02 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# All shall be well and all shall be well and all manner of things shall be well.
# We're doomed!
###

import numpy as np

def getMap():
    #无限的值
    INF_NUM =  999

    # 节点数
    node_num = 6

    #每2个之间相互链接的概率节点
    connectedProbability = 0.6

    # 生成随机权重的邻接矩阵
    tspMap = np.ones((node_num,node_num))*INF_NUM

    #对每个顶点随机
    for i in range(node_num):
        for j in range(i,node_num):
            if i == j:
                tspMap[i,j] = 0
            else:
                if np.random.rand() <= connectedProbability:
                    tspMap[i,j] = np.random.randint(1, 100)
                    tspMap[j,i] = tspMap[i,j]                    
    return tspMap

def testConnetc(map):
    nodeNum = np.shape(map)[0]
    visited = [0 for i in range(nodeNum)]
    for i in range(nodeNum):
        if (visited[i] == 0):
            dfs(map, nodeNum, visited, i);
            break
    if (np.sum(visited) == nodeNum):
        return True
    else:
        return False
def testCycle():
    nodeNum = np.shape(map)[0]
    visited = [0 for i in range(nodeNum)]
    for i in range(nodeNum):
        if (visited[i] == 0):
            dfs(map, nodeNum, visited, i);
            break
    if (np.sum(visited) == nodeNum):
        return True
    else:
        return False

def dfs(map, nodeNum, visited, pos):
    INF_NUM =  999    
    visited[pos] = 1
    for i in range(nodeNum):
        if (visited[i] == 0 and map[pos, i] != INF_NUM):
            dfs(map, nodeNum, visited, i)
        

def getTstMap():
    Tmap  = getMap()
    while(testConnetc(Tmap) == False):
        Tmap  = getMap()
    return Tmap