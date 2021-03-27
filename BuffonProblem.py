# 实例1:蒲丰氏投针实验估算圆周率π的值
# 问题描述：为了求得圆周率π值，在十九世纪后期，有很多人作了这样的试验：
# 将长为2l的一根针任意投到地面上，用针与一组相间距离为2a（ l＜a）的平行线相交的频率代替概率P
# P=2l/πa ---->>> π=2l/Pa=2l/(a(n/N))=2lN/an

# 功能：计算机模拟蒲丰投针，a=4,l=3
# 编写：Rem~   @2020.09.27


import random  # 导入random模块，调用randint
import math  # 导入math模块，调用pi和sin

#   *********初始化*************
needle_len = int(input("请输入针长度半l："))
parallel_width = int(input("请输入平行线半间距a："))
test_num = int(input("请输入实验次数N："))
n = 0
#   *********条件判断*************
if needle_len >= parallel_width:
    print("实验前提条件错误!针长度l应该小于平行线间距a，请重新运行")
else:
    #   *********循环迭代*************
    #   基于均匀分布的随机数生成
    for num in range(0, test_num):
        theta = random.uniform(0, math.pi)  # 生成0~π的随机小数
        x = random.uniform(0, parallel_width)  # 生成0~a的随机小数
        if x <= needle_len * math.sin(theta):  # 投针压线判断条件
            n = n + 1
        else:
            n = n
    #   *********估计结果*************
    P = n / test_num  # 投针概率统计
    pi_res = 2 * needle_len / parallel_width / P  # 计算公式

    print("实验总投针次数为%d，投针压线次数%d" % (test_num, n))
    print("蒲丰氏投针实验模拟计算π的的结果为%.5f" % pi_res)
    print("模拟结果与实际真值绝对误差%.5f,相对误差%.3f %%" % (abs(math.pi - pi_res), abs(math.pi - pi_res) / math.pi * 100))

#   *********残留问题*************
#   投针判断利用循环，可尝试采用矩阵计算提高运算速度
