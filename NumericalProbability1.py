#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 22:59
# @Author  : Rem~
# @File    : NumericalProbability1.py
# @function: 数值概率实例1：
# 设有一半径为r的圆及其外切四边形，向该正方形随机投掷n个点。
# 设落入圆内的点在正方形上均匀分布，因而所投入点落入圆内的概率为πr^2/4r^2，所以当n足够大时，k与n之比就逼近这一概率，即π/4。
# 由此可得使用随机投点法计算π值的数值概率算法。
# 最简方案：具体实现时，设r=1并在第一次象限计算即可。

import random
import math

num = int(input("请输入模拟次数N："))
sum_n = 0
for i in range(0,num):
    # uniform(0, 1) 即[0,1)
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if (pow(x, 2)+pow(y, 2)) < 1:
        sum_n = sum_n +1
P = sum_n/num
pai = P*4
print("数值概率模拟的π值：%.5f" % pai)
print("π值的绝对误差：%.5f，相对误差：%.5f%%" % (abs(math.pi - pai), abs(math.pi - pai)*100/math.pi))


