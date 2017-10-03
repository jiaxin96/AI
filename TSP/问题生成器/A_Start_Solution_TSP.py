#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: e:\code\AI\TSP\问题生成器\A_Start_Solution_TSP.py
# Project: e:\code\AI
# Created Date: Monday, October 2nd 2017, 8:15:36 pm
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
import genMapTools as mt
import primValue as pv
import numpy as np
from genMapTools import INF_NUM


def aSearch(tmap):
    node_num = np.shape(tmap)[0]
    visited = np.zeros(node_num).tolist()
    Q = list()
    Q.append({'index': 0, 'weight': 0, 'gv': 0, 'hv': 0, 'path': []})
    findWay = False
    ans = []
    while len(Q) != 0:
        Q.sort(key=lambda x: x['weight'])
        front = Q[0]
        visited[front['index']] = 1
        del Q[0]
        
        for i in range(0, node_num):
            if tmap[front['index'], i] != INF_NUM and tmap[front['index'], i] != 0:
                visited[i] = 1
                unvmap = mt.genUnvisitedMap(tmap, visited)
                visited[i] = 0
                tp = front['path'].copy()
                tp.append(front['index'])
                hv = pv.calPrimVal(unvmap)
                gv = tmap[front['index'], i] + front['gv']
                Q.append({'index': i, 'weight': hv+gv, 'gv': gv, 'hv': hv, 'path': tp})
                if (i == 0):
                    findWay = True
                    ans = tp
                    break
        if (findWay):
            break
    
    return ans


def main():
    TSP_MAP = mt.getMap()
    return(aSearch(TSP_MAP))


if __name__ == '__main__':
    print(main())