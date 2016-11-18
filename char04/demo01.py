#coding:utf-8

import numpy as np
data1=[6,7.5,8,0,1]#list
arr1=np.array(data1)#numpy.ndarray
# print type(arr1),type(data1)


data2=[[1,2,3,4],[5,6,7,8]]
arr2=np.array(data2)
# print arr2.ndim#2
# print arr2.shape#(2, 4)，各维度大小的元组
# print arr2.dtype#int32，数组数据类型


# print np.zeros(10)
# print np.zeros((3,6))
# print np.empty((2,3,2))#返回一些未被初始化的垃圾值
# print np.arange(15)#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]


arr1=np.array([1,2,3],dtype=np.float64)
arr2=np.array([1,2,3],dtype=np.int32)
# print arr1.dtype,arr2.dtype

arr=np.array([1,2,3,4,5])
float_arr=arr.astype(np.float64)#astype方法显式转换dtype
# print float_arr.dtype


arr=np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
# print arr.astype(np.int32)#浮点数转成整数，小数部分被截断


arr=np.arange(10)
arr_slice=arr[5:8]
arr_slice[:]=64
# print arr_slice


arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print arr2d[0][2],arr2d[0,2]


arr=np.empty((8,4))
for i in range(8):
    arr[i]=i


#花式索引
arr=np.arange(32).reshape((8,4))
# print arr[[1,5,7,2],[0,3,1,2]]
# print arr[[1,5,7,2]][:,[0,3,1,2]]
# print arr[np.ix_([1,5,7,2],[0,3,1,2])]



arr=np.arange(16).reshape((2,2,4))
print arr.transpose((1,0,2))


















