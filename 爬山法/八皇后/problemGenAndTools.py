#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : climbAndSimulatedAnnealing.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/19/17
# @Desc  : 学习使用

import numpy as np

def gen():
    chessBoard = np.zeros((8,8))
    for i in range(8):
        chessBoard[i][np.random.randint(0,8)] = 1;
    return  chessBoard


def moveOneChessInRow(row,board):
    '''
    完成数组的一行循环左移
    :param row:
    :param board:
    :return:
    '''
    board = board.tolist()
    t = board[row][-1]
    del board[row][-1]
    board[row] = [t] + board[row]
    return np.array(board)

def detectConfilctChessNum(board):
    # 横向
    cfCount = 0
    for i in range(8):
        chess_in_row = np.sum(board[i])
        if (chess_in_row <= 1):
            continue
        cfCount += int((chess_in_row-1)*chess_in_row/2)
    # 纵向
    for i in range(8):
        chess_in_col = np.sum(board[:, i])
        if (chess_in_col <= 1):
            continue
        cfCount += int((chess_in_col-1)*chess_in_col/2)
    # 主对角线
    for i in range(8):
        chess_in_main_diagonal = 0
        for j in range(8-i):
            chess_in_main_diagonal += board[j+i, j]
        if chess_in_main_diagonal <= 1:
            continue

        cfCount += int((chess_in_main_diagonal-1)*chess_in_main_diagonal/2)
    for i in range(7):
        chess_in_main_diagonal = 0
        for j in range(7-i):
            chess_in_main_diagonal += board[j, j+i+1]
        if chess_in_main_diagonal <= 1:
            continue
        cfCount += int((chess_in_main_diagonal-1)*chess_in_main_diagonal/2)

    # 副对角线
    for i in range(8):
        chess_in_minor_diagonal = 0
        for j in range(8-i):
            chess_in_minor_diagonal += board[j+i,7-j]
        if chess_in_minor_diagonal <= 1:
            continue
        cfCount += int((chess_in_minor_diagonal-1)*chess_in_minor_diagonal/2)
    for i in range(7):
        chess_in_minor_diagonal = 0
        for j in range(7-i):
            chess_in_minor_diagonal += board[j,6-j-i]
        if chess_in_minor_diagonal <= 1:
            continue
        cfCount += int((chess_in_minor_diagonal-1)*chess_in_minor_diagonal/2)
    return  cfCount
# test
if __name__ == '__main__':
    print(gen())