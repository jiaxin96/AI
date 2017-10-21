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
    row = int(blank_index / 3)
    col = blank_index % 3
    if direction == 0:
        # 上移
        if row > 0:
            t = board[row*3+col]
            board[row*3+col] = board[row*3+col-3]
            board[row * 3 + col - 3] = t
            return True
    elif direction == 1:
        # 下移
        if row < 2:
            t = board[row * 3 + col]
            board[row * 3 + col] = board[row * 3 + col + 3]
            board[row * 3 + col + 3] = t
            return True
    elif direction == 2:
        # 左移
        if col > 0:
            t = board[row * 3 + col]
            board[row * 3 + col] = board[row * 3 + col-1]
            board[row * 3 + col - 1] = t
            return True
    elif direction == 3:
        # 右移
        if col < 2:
            t = board[row * 3 + col]
            board[row * 3 + col] = board[row * 3 + col + 1]
            board[row * 3 + col + 1] = t
            return True
    return False

def gen(step_num):
    '''
    生成地图
    :param step_num:随机移动的次数
    :return:生成好的初始局面
    '''
    end_state_list = [x for x in range(1,9)]
    end_state_list.append(0)
    init_board = np.array(end_state_list)
    for i in range(step_num):
        move(np.random.randint(0,4), init_board)
    return  init_board


def get_error_position_num(board):
    '''
    错码数
    :param board:
    :return:
    '''
    error_position_num = 0
    for i in range(9):
        if (board[i] == 0):
            continue
        if (board[i] != i+1):
            error_position_num += 1
    return error_position_num

def get_all_chess_manhattan_dis(board):
    '''
    曼哈顿距离
    :param board:
    :return:
    '''
    all_chess_manhattan_dis = 0
    for i in range(9):
        if (board[i] == 0):
            continue
        all_chess_manhattan_dis += abs(i%3 - (board[i]-1)%3)
        all_chess_manhattan_dis += abs(int(i/3) - int((board[i]-1)/3))
    return all_chess_manhattan_dis


def equal_board(b1, b2):
    for i in range(9):
        if (b1[i] != b2[i]):
            return  False
    return True


def evaluation(board):
    return get_error_position_num(board)+get_all_chess_manhattan_dis(board)


if __name__ == '__main__':
    init_board = gen(1)
    print(init_board)
    print(get_all_chess_manhattan_dis(init_board))
    print(get_error_position_num(init_board))