# coding:utf-8

# Numpy高级应用
# ndarray对象的内部机理
# 1.一个指向数组的指针
# 2.数据类型(dtype)
# 3.一个表示数组形状(shape)的元祖
# 4.一个跨度元祖(stride)

import numpy as np

arr = np.arange(15).reshape((5, 3))
# print arr
# print arr.ravel()#不产生副本
# print arr.flatten()#产生副本

from numpy.random import randn

arr = randn(5, 2)
# print arr

first, second, third = np.split(arr, [4, 3])

# print first
# print second
# print third

# from numpy cimport ndarray, float64_t
