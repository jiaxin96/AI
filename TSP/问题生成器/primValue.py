#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\AI\TSP\问题生成器\primValue.py
# Project: e:\code\AI
# Created Date: Monday, October 2nd 2017, 12:25:02 am
# Author: JX
# -----
# Last Modified: Wed Oct 04 2017
# Modified By: JX
# -----
# Copyright (c) 2017 SYSU-SDCS-RJX
# 
# 学习使用
# github地址:https://github.com/jiaxin96
###

from genMapTools import INF_NUM
import numpy as np


def calPrimVal(vexs):
    node_num = np.shape(vexs)[0]
    mst = np.zeros(node_num)               # 连通分量，初始只有第一个顶点，当全部元素为1后，说明连通分量已经包含所有顶点
    lowcost = vexs[0].tolist()
    
    # 初始化第一个顶点在mst中
    mst[0] = 0  # 记录加入mst的的节点的父节点
    lowcost[0] = 0  # 距离顶点1的最小距离
    
    mstCost = 0

    for i in range(1, node_num):
        lowcost[i] = vexs[0, i]
        mst[i] = 1
    for i in range(1, node_num):
        # 没有加入mst中的最小距离
        minCost = INF_NUM
        # minCost的索引
        minIndex = 0
        isFind = False
        
        for j in range(1, node_num):
            # 从第二开始寻找最小权值边 和对应的索引
            if (lowcost[j] < minCost and lowcost[j] != 0):
                minCost = lowcost[j]
                minIndex = j
                isFind = True
        
        if not isFind:
            break
        mstCost += minCost
        lowcost[minIndex] = 0

        for j in range(1, node_num):
            if vexs[minIndex, j] < lowcost[j]:
                lowcost[j] = vexs[minIndex, j]
                mst[j] = minIndex
    
    return mstCost