#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : testDraw.py
# @Author: https://github.com/jiaxin96
# @Date  : 10/21/17
# @Desc  : 学习使用

from pyecharts import Line

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
attr2 = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr2, v2, is_smooth=True, mark_line=["max", "average"])
line.render()