#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : repeatTest.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/21/17
# @Desc  : 学习使用
from pyecharts import Bar, Line
import os

def drawBar(title,xLables, datas, direname):
    bar = Bar(title)
    bar.add(title, xLables, datas)
    bar.render(direname+"/"+title+".html")

def drawLines(title, linenames,timeSeqs, datas, direname):
    line = Line(title)
    for i in range(len(linenames)):
        line.add(linenames[i], timeSeqs[i], datas[i])
    line.render(direname+"/"+title+".html")