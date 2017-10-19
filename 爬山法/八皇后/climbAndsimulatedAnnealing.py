#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : climbAndsimulatedAnnealing.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/19/17
# @Desc  : 学习使用

import  八皇后.problemGenAndTools as pt


import numpy as np
from datetime import datetime


def simulated_annealing(initBoard):
    init_board = initBoard
    cur_board = init_board.copy()
    step = 0
    node_num = 0
    row_index = [x for x in range(8)]
    while True:
        neighbor = []
        cur_confilct_num = pt.detectConfilctChessNum(cur_board)
        step += 1
        np.random.shuffle(row_index)
        for i in row_index:
            cur_next = cur_board
            for j in range(7):
                cur_next = pt.moveOneChessInRow(i,cur_next)
                node_num += 1
                if (cur_confilct_num > pt.detectConfilctChessNum(cur_next)):
                    neighbor.append(cur_next)
                    break
            if (len(neighbor) != 0):
                break
        if (len(neighbor) == 0):
            local_smallest = cur_board
            break
        cur_board = neighbor[0]
    return  local_smallest, step , node_num


def simple_climb_first_select(initBoard):
    init_board = initBoard
    cur_board = init_board.copy()
    step = 0
    node_num = 0
    row_index = [x for x in range(8)]
    while True:
        neighbor = []
        cur_confilct_num = pt.detectConfilctChessNum(cur_board)
        step += 1
        np.random.shuffle(row_index)
        for i in row_index:
            cur_next = cur_board
            for j in range(7):
                cur_next = pt.moveOneChessInRow(i,cur_next)
                node_num += 1
                if (cur_confilct_num > pt.detectConfilctChessNum(cur_next)):
                    neighbor.append(cur_next)
                    break
            if (len(neighbor) != 0):
                break
        if (len(neighbor) == 0):
            local_smallest = cur_board
            break
        cur_board = neighbor[0]
    return  local_smallest, step , node_num

def simple_climb_optimistic(initBoard):
    init_board = initBoard
    cur_board = init_board.copy()
    step = 0
    node_num = 0
    while True:
        cur_confilct_num = pt.detectConfilctChessNum(cur_board)
        min_conflict_num = cur_confilct_num
        min_board = cur_board
        step += 1
        for i in range(8):
            cur_next = cur_board
            for j in range(7):
                cur_next = pt.moveOneChessInRow(i, cur_next)
                cur_next_conflict_num = pt.detectConfilctChessNum(cur_next)
                node_num += 1
                if (min_conflict_num > cur_next_conflict_num):
                    min_board = cur_next.copy()
                    min_conflict_num = cur_next_conflict_num
        if (min_conflict_num == cur_confilct_num):
            local_smallest = cur_board
            break
        cur_board = min_board
    return  local_smallest, step , node_num

def simple_climb_randomReboot(initBoard, node_num, rebootNum):
    init_board = initBoard
    cur_board = init_board.copy()
    step = 0
    row_index = [x for x in range(8)]
    while True:
        neighbor = []
        cur_confilct_num = pt.detectConfilctChessNum(cur_board)
        step += 1
        np.random.shuffle(row_index)
        for i in row_index:
            cur_next = cur_board
            for j in range(7):
                cur_next = pt.moveOneChessInRow(i,cur_next)
                node_num += 1
                if (cur_confilct_num > pt.detectConfilctChessNum(cur_next)):
                    neighbor.append(cur_next)
                    break
            if (len(neighbor) != 0):
                break
        if (len(neighbor) == 0):
            local_smallest = cur_board
            break
        cur_board = neighbor[0]
    if (pt.detectConfilctChessNum(local_smallest) != 0):
        rebootNum += 1
        return simple_climb_randomReboot(initBoard, node_num, rebootNum)
    return  local_smallest, step, node_num, rebootNum



if __name__ == '__main__':
    initBoard = pt.gen()
    sTime = datetime.now()
    (ansBoard, ansStep, node_num) = simple_climb_first_select(initBoard)
    eTime = datetime.now()
    print("首选爬山法的结果为:")
    print(ansBoard)
    print("最终冲突数为:" + str(pt.detectConfilctChessNum(ansBoard)))
    print("解的深度为:"+ str(ansStep))
    print("生成节点数为:"+ str(node_num))
    print("用时%dms"%(eTime-sTime).microseconds)

    sTime = datetime.now()
    (ansBoard, ansStep, node_num) = simple_climb_optimistic(initBoard)
    eTime = datetime.now()
    print("最陡上升爬山法的结果为:")
    print(ansBoard)
    print("最终冲突数为:" + str(pt.detectConfilctChessNum(ansBoard)))
    print("解的深度为:"+ str(ansStep))
    print("生成节点数为:"+ str(node_num))
    print("用时%dms"%(eTime-sTime).microseconds)

    sTime = datetime.now()
    cur_node_num = 0
    (ansBoard, ansStep, node_num, reboot_num) = simple_climb_randomReboot(initBoard, 0, 0)
    eTime = datetime.now()
    print("随机重启爬山法的结果为:")
    print(ansBoard)
    print("最终冲突数为:" + str(pt.detectConfilctChessNum(ansBoard)))
    print("解的深度为:"+ str(ansStep))
    print("生成节点数为:"+ str(node_num))
    print("重启次数为:"+str(reboot_num))
    print("用时%dms"%(eTime-sTime).microseconds)

