#!/usr/bin/env python
# -*- coding:utf-8 -*-

from numpy import *

# 创建一个4*4的随机数组

array4_4 = random.rand(4, 4)

'''
在numpy中 matrix 和arrary是不同的两种数据类型 可以使用mat函数将数组转换成矩阵
'''

randMat = mat(random.rand(4,4))

#矩阵求逆
invMat = randMat.I

#矩阵和其逆矩阵相乘是单位矩阵
print(array4_4)

print(randMat)

print(invMat)

print(randMat*invMat)


#创建4*4的单位矩阵
print(eye(4))

