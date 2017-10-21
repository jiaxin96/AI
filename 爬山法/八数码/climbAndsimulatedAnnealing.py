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
    coolingRate = 0.9997
    return  init_temperature*(coolingRate**time_count)


def simulated_annealing(initBoard):
    cur_board = initBoard.copy()
    step = 0
    directions = [0,1,2,3]
    time_count = 0
    temperature = schdule(0)
    while temperature > 0.0003:
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
    local_smallest = cur_board
    return local_smallest, step


def simple_climb_first_select(initBoard):
    cur_board = initBoard.copy()
    step = 0
    directions = [0,1,2,3]
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

def simple_climb_optimistic(initBoard):
    cur_board = initBoard.copy()
    step = 0
    directions = [0,1,2,3]

    while True:
        cur_evaluation = pt.evaluation(cur_board)
        min_board = cur_board
        min_board_evaluation = cur_evaluation
        neighbor = []
        step += 1
        for direction in directions:
            next_board = cur_board.copy()
            if pt.move(direction, next_board):
                next_board_evaluation = pt.evaluation(next_board)
                if (next_board_evaluation<min_board_evaluation):
                    min_board_evaluation = next_board_evaluation
                    min_board = next_board
        if (min_board_evaluation == cur_evaluation):
            local_smallest = min_board
            break
        cur_board = min_board
    return local_smallest, step


def once_test():
    init_board = pt.gen(100)
    print(init_board)
    print(pt.evaluation(init_board))
    (ans_board, ans_step) = simple_climb_first_select(init_board)
    print(ans_board)
    print(pt.evaluation(ans_board))
    print(ans_step)
    (ans_board, ans_step) = simple_climb_optimistic(init_board)
    print(ans_board)
    print(pt.evaluation(ans_board))
    print(ans_step)
    (ans_board, ans_step) = simulated_annealing(init_board)
    print(ans_board)
    print(pt.evaluation(ans_board))
    print(ans_step)

def one_case_test():
    init_board = np.array([3, 8, 1, 4, 5, 6, 7, 2, 0])
    print(pt.evaluation(init_board))
    pt.move(3, init_board)
    print(init_board)
    print(pt.evaluation(init_board))


if __name__ == '__main__':
    once_test()