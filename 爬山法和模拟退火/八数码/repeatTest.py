#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : repeatTest.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/21/17
# @Desc  : 学习使用

import 八数码.climbAndsimulatedAnnealing as gm
import common.draw as dr
import os
import math
def runTest():
    # 首选爬山法, 最陡上升法, 模拟退火法
    # 估值 解的深度 节点数 耗时
    test_case  = 1000
    success_num = [0, 0, 0]
    time_cost = [[],[],[]]
    time_seqs = [[],[],[]]
    path_cost = [0, 0, 0]
    for i in range(test_case):
        tans = gm.once_test()
        for j in range(3):
            if (tans[j][0] == 0):
                success_num[j] += 1
                path_cost[j] += tans[j][2]
                time_cost[j].append(tans[j][3])

    for i in range(3):
        time_seqs[i] = [x for x in range(success_num[i])]
        path_cost[i] = 0 if success_num[i] == 0 else math.log10(path_cost[i]/success_num[i])
        success_num[i] = success_num[i]/test_case
    dr.drawBar("成功率", ["首选爬山法", "最陡上升法", "模拟退火法"], success_num, os.path.dirname(os.path.realpath(__file__)))
    dr.drawBar("成功的情况下平均生成节点数", ["首选爬山法", "最陡上升法", "模拟退火法"], path_cost, os.path.dirname(os.path.realpath(__file__)))
    dr.drawLines("成功情况的耗时情况 单位ms",["首选爬山法", "最陡上升法", "模拟退火法"], time_seqs, time_cost, os.path.dirname(os.path.realpath(__file__)))
if __name__ == '__main__':
    runTest()