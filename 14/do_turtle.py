#!usr/bin/env python3
# -*- coding: utf-8 -*-

# 导入turtle包的所有内容:
from turtle import *

# 设置笔刷宽度:
width(6)

# 前进:
forward(200)
# 右转90度:
right(90)

# 笔刷颜色:
pencolor('red')
forward(100)
right(90)

pencolor('green')
forward(200)
right(90)

pencolor('blue')
forward(100)
right(90)

# 调用done()让窗口进入消息循环, 等待被关闭，否则将立刻关闭窗口:
done()