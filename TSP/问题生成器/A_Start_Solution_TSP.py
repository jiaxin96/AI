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
    start_node = 0
    node_num = np.shape(tmap)[0]
    visited = np.zeros(node_num).tolist()
    Q = list()
    Q.append({'index': start_node, 'weight': 0, 'gv': 0, 'hv': 0, 'path': []})
    findWay = False
    ans = []
    while len(Q) != 0:
        Q.sort(key=lambda x: x['weight'])
        front = Q[0]
        visited[front['index']] = 1
        del Q[0]
        
        for i in range(0, node_num):
            if tmap[front['index'], i] == 0:
                continue
            if tmap[front['index'], i] != INF_NUM:
                if visited[i] == 0:
                    visited[i] = 1
                    unvmap = mt.genUnvisitedMap(tmap, visited)
                    visited[i] = 0
                    tp = front['path'].copy()
                    tp.append(front['index'])
                    hv = pv.calPrimVal(unvmap) + tmap[start_node, i]
                    gv = tmap[front['index'], i] + front['gv']
                    Q.append({'index': i, 'weight': hv+gv, 'gv': gv, 'hv': hv, 'path': tp})
                    # if (i == start_node and np.sum(visited) >= node_num):
                    #     findWay = True
                    #     ans = tp
                    #     break
                elif i == start_node and len(front['path']) >= node_num-1:
                    ans = front['path'] + [front['index']]
                    findWay = True
            if (findWay):
                break
    
    return ans


def main():
    TSP_MAP = mt.getMap()

    return(TSP_MAP, aSearch(TSP_MAP))


if __name__ == '__main__':
    solution = main()
    print("地图邻接矩阵:")
    print(solution[0])
    print("TSP路径:")
    print(solution[1])