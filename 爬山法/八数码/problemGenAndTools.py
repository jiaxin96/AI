#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : climbAndSimulatedAnnealing.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/19/17
# @Desc  : 学习使用

import numpy as np

def move(direction,board):
    '''
    移动一次
    '''
    blank_index = board.tolist().index(0)
    row = blank_index / 3
    col = blank_index % 3
    if direction == 0:
        if row > 0:
            t = board[row*3+col]
            board[row*3+col] = board[row*3+col-3]
            board[row * 3 + col - 3] = t
    elif direction == 1:
        if row < 2:
            t = board[row * 3 + col]
            board[row * 3 + col] = board[row * 3 + col + 3]
            board[row * 3 + col + 3] = t

def gen():
    end_state_list = [x for x in range(1,9)]
    end_state_list.append(0)
    init_board = np.array(end_state_list)
