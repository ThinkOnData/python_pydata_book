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
# print arr.transpose((1,0,2))


points=np.arange(-5,5,0.01)#1000个间隔相等的点
xs,ys=np.meshgrid(points,points)

# print xs
# print ys


import matplotlib.pyplot as plt
z=np.sqrt(xs**2+ys**2)
# print z


from pylab import *
# show(plt.imshow(z,cmap=plt.cm.gray))


#将条件逻辑表述为数组运算
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=[(x if c else y)for x,y,c in zip(xarr,yarr,cond)]
# print result


result=np.where(cond,xarr,yarr)
# print result


arr=randn(4,4)
# print arr
# print np.where(arr>0,2,-2)
# print np.where(arr>0,2,arr)#只将正值设置为2



#数学和统计方法
arr=np.random.randn(5,4)#正态分布的数据
# print arr.mean()
# print np.mean(arr)
# print arr.std()
# print arr.sum()


arr=randn(5,3)
# print arr
# print arr.sort(0)


large_arr=randn(1000)
large_arr.sort()
# print large_arr[int(0.05*len(large_arr))]#5%分位数


ints=np.array([3,3,3,2,2,1,1,4,4])
# print np.unique(ints)#找出数组中的唯一值并返回已排序的结果


values=np.array([6,0,0,3,2,5,6])
# print np.in1d(values,[2,3,6])[ True False False  True  True False  True]


arr=np.arange(10)
# np.save('some_arr',arr)
# print np.load('some_arr.npy')

brr=np.arange(20)
# np.savez('array_archive',a=arr,b=brr)
# arch=np.load('array_archive.npz')
# print arch['b']


arr=np.loadtxt("array_ex.txt",delimiter=",")
# print arr


from numpy.linalg import inv,qr
X=randn(5,5)
mat=X.T.dot(X)
# print mat.dot(inv(mat))

q,r=qr(mat)
# print q
# print r


from random import normalvariate
N=1000000
samples=[normalvariate(0,1) for _ in xrange(N)]
np.random.normal(size=N)


#随机漫步
import random
position=0
walk=[position]
steps=1000
for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position +=step
    walk.append(position)

# show(plot(walk))


nsteps=1000
draws=np.random.randint(0,2,size=nsteps)#randint()上下限范围的随机整数
steps=np.where(draws>0,1,-1)
walk=steps.cumsum()
# print walk.min()
# print walk.max()

#至少漫步多久才能距离初始0点至少10步远（任一方向）
# print (np.abs(walk)>=10).argmax()


#一次模拟多个随机漫步
nwalks=5000
nsteps=1000
draws=np.random.randint(0,2,size=(nwalks,nsteps))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)
# print walks

hits30=(np.abs(walks)>=30).any(1)
# print hits30
# print hits30.sum()#达到30或-30的数量



crossing_times=(np.abs(walks[hits30])>=30).argmax(1)
# print crossing_times.mean()


steps=np.random.normal(loc=0,scale=0.25,size=(nwalks,nsteps))
# print steps
