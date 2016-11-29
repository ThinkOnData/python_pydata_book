#coding:utf-8

#绘图和可视化

import numpy as np
from matplotlib.pyplot import plot, show

# show(plot(np.arange(10)))

import matplotlib.pyplot as plt
fig=plt.figure()

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)


from numpy.random import randn
show(plt.plot(randn(50).cumsum(),"k--"))




