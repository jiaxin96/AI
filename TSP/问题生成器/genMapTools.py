#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /home/jx/Desktop/codes/AI/TSP/问题生成器/genMap.py
# Project: /home/jx/Desktop/codes/AI/TSP
# Created Date: Saturday, September 30th 2017, 7:50:25 pm
# Author: JX
# -----
# Last Modified: Wed Oct 04 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# All shall be well and all shall be well and all manner of things shall be well.
# We're doomed!
###

import numpy as np

#无限的值
INF_NUM = 999


# 节点的个数
node_num = 5


#地理分布边长 km
geo_len = 100


def getMap():

    # 每2个之间相互链接的概率节点
    connectedProbability = 1

    # 生成随机权重的邻接矩阵
    tspMap = np.ones((node_num, node_num))*INF_NUM

    # 对每个顶点随机
    for i in range(node_num):
        for j in range(i, node_num):
            if i == j:
                tspMap[i, j] = 0
            else:
                if np.random.rand() <= connectedProbability:
                    tspMap[i, j] = np.random.randint(1, 100)
                    tspMap[j, i] = tspMap[i, j]
    return tspMap


def testConnetc(map):
    nodeNum = np.shape(map)[0]
    visited = [0 for i in range(nodeNum)]
    for i in range(nodeNum):
        if (visited[i] == 0):
            dfs(map, nodeNum, visited, i)
            break
    if (np.sum(visited) == nodeNum):
        return True
    else:
        return False


def testCycle(Tmap):
    nodeNum = np.shape(Tmap)[0]
    visited = [0 for i in range(nodeNum)]
    for i in range(nodeNum):
        if (visited[i] == 0):
            dfs(Tmap, nodeNum, visited, i);
            break
    if (np.sum(visited) == nodeNum):
        return True
    else:
        return False


def genUnvisitedMap(TSPmap, visited):
    Tmap = TSPmap.copy()
    delNum = 0
    for i in range(len(visited)):
        if (visited[i] == 1):
            Tmap = np.delete(Tmap, i-delNum, axis=0)
            Tmap = np.delete(Tmap, i-delNum, axis=1)
            delNum += 1
    return Tmap


def dfs(map, nodeNum, visited, pos):
    visited[pos] = 1
    for i in range(nodeNum):
        if (visited[i] == 0 and map[pos, i] != INF_NUM):
            dfs(map, nodeNum, visited, i)
        

def getTspMap():
    Tmap  = getMap()
    while(testConnetc(Tmap) == False or testCycle(Tmap) == False):
        Tmap  = getMap()
    return Tmap


def getDistribution():
    geo_map = []
    for i in range(node_num):
        x = np.random.randint(0, geo_len)
        y = np.random.randint(0, geo_len)
        geo_map.append((i, x, y))
    return geo_map

def test():
    a = getTspMap()
    print(a)
    visited = [0 for i in range(len(a))]
    visited[1] = 1
    visited[2] = 1    
    print(genUnvisitedMap(a, visited))
    print(getDistribution())


def main():
    test()

if __name__ == '__main__':
    main()