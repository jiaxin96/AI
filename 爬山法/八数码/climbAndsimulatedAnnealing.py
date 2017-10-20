#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : climbAndsimulatedAnnealing.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/21/17
# @Desc  : 学习使用

import 八数码.problemGenAndTools as pt
import numpy as np
import math

def schdule(time_count):
    init_temperature = 1000
    coolingRate = 0.9999
    return  init_temperature*(coolingRate**time_count)


def simulated_annealing(initBoard):
    cur_board = initBoard.copy()
    step = 0
    directions = [1,2,3,4]
    time_count = 0

    while True:
        temperature = schdule(time_count)
        time_count += 1

        cur_evaluation = pt.evaluation(cur_board)
        neighbor = []
        step += 1
        np.random.shuffle(directions)
        for direction in directions:
            next_board = cur_board.copy()
            if pt.move(direction, next_board):
                deltE = cur_evaluation - pt.evaluation(next_board)
                if (deltE > 0 or np.random.rand() < math.exp(float(deltE)/float(temperature))):
                    neighbor.append(next_board)
                    break
        if (len(neighbor) != 0):
            cur_board = neighbor[0]
        else:
            local_smallest = cur_board
            break
    return local_smallest, step


def simple_climb_first_select(initBoard):
    cur_board = initBoard.copy()
    step = 0
    directions = [1,2,3,4]
    while True:
        cur_evaluation = pt.evaluation(cur_board)
        neighbor = []
        step += 1
        np.random.shuffle(directions)
        for direction in directions:
            next_board = cur_board.copy()
            if pt.move(direction, next_board):
                if (pt.evaluation(next_board) < cur_evaluation):
                    neighbor.append(next_board)
                    break
        if (len(neighbor) != 0):
            cur_board = neighbor[0]
        else:
            local_smallest = cur_board
            break
    return local_smallest, step


def once_test():
    init_board = pt.gen(100)
    print(pt.evaluation(init_board))
    print(init_board)
    (ans_board, ans_step) = simple_climb_first_select(init_board)
    print(ans_board)
    print(pt.evaluation(ans_board))
    print(ans_step)

if __name__ == '__main__':
    once_test()